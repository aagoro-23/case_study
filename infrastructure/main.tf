module "blackrock_case_study"{
    source     = "./modules/"
    aws_region = var.aws_region
    ecr_repo_api = var.ecr_repo_api
    image_tag = var.image_tag
    cluster_name = var.cluster_name
}
