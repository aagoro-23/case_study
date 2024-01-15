# BlackRock: Backend &amp; cloud engineer case study
## AI Labs: Senior Backend and Cloud Engineer, Associate
### Aaron Gonzalez

## About this repo
This repository contains the code for the backend of an application that simulates 20 timesteps of a time-discrete dynamical system defined by the following equations:

$x <sub>$n+1$</sub>$= x<sub>$n$</sub> + x<sub>$n$</sub> \sigma(y<sub>$n$</sub> - x<sub>$n$</sub>) \cdot \Delta t$

$y$<sub>$n+1$</sub>$= y$<sub>$n$</sub>$ + (x$<sub>$n$</sub>$( \rho - z$<sub>$n$</sub>$ )- z$<sub>$n$</sub>$y$<sub>$n$</sub>$)\cdot \Delta t$
$z$<sub>$n+1$</sub>$= z$<sub>$n$</sub>$ + (x$<sub>$n$</sub>$y$<sub>$n$</sub>$- \beta z$<sub>$n$</sub>$)\cdot \Delta t$

Where $x$<sub>$n$</sub>, $y$<sub>$n$</sub>, and $z$<sub>$n$</sub> represent the position of a three-dimensional space at time $n$, $\Delta t$ represents a discrete time step size (i.e., the amount of time between time steps $n$ and $n+1$) and $\rho, \beta$, and $\sigma$ are free parameters chosen by the user that affect the behaviours of the system. Starting with an arbitrarily selected initial condition,$ (x,y,z) $ , the equations above may be applied repeatedly to approximate the point’s position at any future time, $N$ .

It also contains IAC code to spin up the necessary taks ECR repository, ECS task definitions and service, and an application load balancer to be able to access the application on the cloud.

## API Usage

This API has two GET methods.

1. GET / will return a string with a welcoming message
2. GET /calculation will return a Json containing 20 iterative calculations for the time-discrete dynamical system.
To use simply perform a GET request on /calculation together with a query
For example:
```
GET /calculation?x0=1&y0=2&z0=3&sigma=4&rho=5&beta=1&delta_t=2
```

### Structure
This repo contains the code for the backend inside of the backend folder, and the code to set up the infrastructure in the infrastructure folder

## Setting up this repo
---
### Prerequisites
To set up this repository, you will need:
1. Python with pip
2. Docker
3. Terraform
4. An AWS account you have access to in order to create infrastructure using Terraform 
5. AWS CLI
6. An already running ECS cluster to deploy the application
---
### Setting up the backend code
First we need to create a virtual environment using Python. 
To do this, change directories to the `backend` folder, create a virtual environment, and install the requirements using pip. This final step should install the latest version for all the requirements of this code.

```
cd backend
python -m pyenv .env
source activate ./.env/bin/activate
pip install -r ./requirements/requirements.txt
```

**Note:** In a production environment we might want to lock the versions of the requirements in order to avoid potential conflicts in the future. 

### Testing

#### Unit testing

This repo uses pytest to perform unit tests. To test the functions of the application, simply run:

`python -m pytest -s -vv ./tests`

#### Local testing

To test the code locally, we can activate the uvicorn server and expose it on our `localhost` using the following command:

`uvicorn app.main:app --host 0.0.0.0 --port 80`

Additionally, we can also test the application inside of a Docker container. To do this simply run the following commands:

```
docker build -t fastapi-app .
docker run -p 80:80 fastapi-app
```

To test the application locally, 

## Infrastructure
Change directories to `infrastructure` and initialise your Terraform modules.
`terraform init`

After that, either create a new ECR repository manually, or use the terraform module located in `infrastructure/modules/api_ecr.tf`.

Once the repository has been created, we need to submit our Docker image to it. To do this simmply make sure you have the right AWS credentials to be able to interact with your AWS account and then execute the following commands:

```
docker login -u AWS -p $(aws ecr get-login-password --region <aws_region>) <aws_account>.dkr.ecr.<aws_region>.amazonaws.com
docker images
```
From the output of `docker images` identify the `image_id` of the image generated on for this app. Then run the next command:

`docker tag <image_id> <aws_account>.dkr.ecr.<aws_region>.amazonaws.com/<repository>:<tag>`

Following this, we need to modify a file located in `infrastructure/variables/case_study.tfvars`. Simply add the required fields to this file. For example:
```
aws_region = "<aws_region>"
ecr_repo_api = "<aws_account>.dkr.ecr.<aws_region>.amazonaws.com/<repository>"
image_tag = "latest"
cluster_name = "<already_existing_ecs_cluster_name>"
```
Note, the image_tag will be `latest` by default. 

Once this is done, we can get a terraform plan to verify that the infrastructure being created is correct by running the following commmand:
`terraform plan -var-file="./variables/case_study.tfvars" `

Finally, apply the infrastructure using the following command:
`terraform apply -var-file="./variables/case_study.tfvars" `

Once this is done, you should be able to access the API on the load balancer's DNS.