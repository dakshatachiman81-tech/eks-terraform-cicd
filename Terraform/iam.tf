data "aws_caller_identity" "current" {}

data "aws_iam_policy_document" "aws_load_balancer_controller_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type = "Federated"

      identifiers = [
        "arn:aws:iam::${data.aws_caller_identity.current.account_id}:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/787E8121E1490234BA8766716D6ED19F"
      ]
    }

    actions = [
      "sts:AssumeRoleWithWebIdentity"
    ]

    condition {
      test     = "StringEquals"
      variable = "oidc.eks.ap-south-1.amazonaws.com/id/787E8121E1490234BA8766716D6ED19F:aud"
      values   = ["sts.amazonaws.com"]
    }

    condition {
      test     = "StringEquals"
      variable = "oidc.eks.ap-south-1.amazonaws.com/id/787E8121E1490234BA8766716D6ED19F:sub"
      values = [
        "system:serviceaccount:kube-system:aws-load-balancer-controller"
      ]
    }
  }
}

resource "aws_iam_role" "aws_load_balancer_controller" {
  name = "AmazonEKSLoadBalancerControllerRole"

  assume_role_policy = data.aws_iam_policy_document.aws_load_balancer_controller_assume_role.json
}

resource "aws_iam_policy" "aws_load_balancer_controller" {
  name   = "AWSLoadBalancerControllerIAMPolicy"
  policy = file("${path.module}/iam_policy.json")
}

resource "aws_iam_role_policy_attachment" "aws_load_balancer_controller" {
  role       = aws_iam_role.aws_load_balancer_controller.name
  policy_arn = aws_iam_policy.aws_load_balancer_controller.arn
}