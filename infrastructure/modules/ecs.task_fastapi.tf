resource "aws_ecs_task_definition" "fastapi_task" {
  family                   = "fastapi_task" 
  container_definitions    = <<DEFINITION
  [
    {
      "name": "fastapi",
      "image": "${var.ecr_repo_api}:${var.image_tag}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp",
          "appProtocol": "http"
        }
      ],
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
  requires_compatibilities = ["EC2"]
  network_mode             = "awsvpc"
  memory                   = 2048
  cpu                      = 1024
  execution_role_arn       = "${aws_iam_role.ecs_task_role_fastapi.arn}"
}

resource "aws_ecs_service" "ecs_api_service" {
  name            = "ecs-fastapi-service"
  cluster         = "${var.cluster_name}" #Reference to already existing ECS
  task_definition = "${aws_ecs_task_definition.fastapi_task.arn}"
  launch_type     = "EC2"
  desired_count   = 1

  load_balancer {
    target_group_arn = "${aws_lb_target_group.target_group.arn}"
    container_name   = "fastapi"
    container_port   = 80
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_b.id}", "${aws_default_subnet.default_subnet_c.id}"]
    security_groups  = ["${aws_security_group.service_security_group.id}"]
  }
}