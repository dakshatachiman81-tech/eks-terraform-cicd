data "aws_iam_policy_document" "github_actions_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type = "Federated"

      identifiers = [
        "arn:aws:iam::099739122394:oidc-provider/token.actions.githubusercontent.com"
      ]
    }

    actions = [
      "sts:AssumeRoleWithWebIdentity"
    ]

    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }

    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = [
        "repo:dakshatachiman81-tech/eks-terraform-cicd:ref:refs/heads/main"
      ]
    }
  }
}

resource "aws_iam_role" "github_actions" {
  name = "GitHubActionsEKSDeployRole"

  assume_role_policy = data.aws_iam_policy_document.github_actions_assume_role.json
}