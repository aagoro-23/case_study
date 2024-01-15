resource "aws_iam_role" "ecs_task_role_fastapi" {
  name               = "ecs_task_role_fastapi"
  assume_role_policy = "${data.aws_iam_policy_document.assume_role_policy.json}"
}