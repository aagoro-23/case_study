variable "aws_region" {
    type = string
    description = "Region to create aws resources in"
}

variable "ecr_repo_api"{
    type = string
    description = "The ECR repo that contains the image for fast api"
}

variable "image_tag"{
    type = string
    description = "The tag for the image in the ECR repo for fastapi"
    default = "latest"
}

variable "cluster_name"{
    type = string
    description = "The existing ECS cluster"
}