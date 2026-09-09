module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "21.10.1"

  name               = var.cluster_name
  kubernetes_version = var.kubernetes_version

  endpoint_public_access = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  enable_cluster_creator_admin_permissions = true

  access_entries = {
    github_actions = {
      principal_arn = aws_iam_role.github_actions.arn

      policy_associations = {
        admin = {
          policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"

          access_scope = {
            type = "cluster"
          }
        }
      }
    }
  }

  addons = {
    vpc-cni = {
      most_recent    = true
      before_compute = true
    }

    kube-proxy = {
      most_recent = true
    }

    coredns = {
      most_recent = true
    }
  }

  eks_managed_node_groups = {
    devops_nodes = {
      name = "devops-node-group"

      instance_types = ["t3.small"]

      min_size     = 1
      max_size     = 2
      desired_size = 1

      capacity_type = "ON_DEMAND"

      labels = {
        Environment = "dev"
        Project     = "eks-terraform-cicd"
      }
    }
  }

  tags = {
    Project = "eks-terraform-cicd"
  }
}