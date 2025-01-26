# Create a Lambda function called myLambdaFunction
resource "aws_lambda_function" "myLambdaFunction" {
    filename = data.archive_file.zip.output_path
    source_code_hash = data.archive_file.zip.output_base64sha256
    function_name = "myLambdaFunction"
    role = aws_iam_role.iam_for_lambda.arn
    handler = "function.handler"
    runtime = "python3.10"
}

# Create an IAM role for our Lambda function
resource "aws_iam_role" "iam_for_lambda" {
    name = "iam_for_lambda"

    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
            "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
}
EOF
}

resource "aws_iam_policy" "iam_policy_for_resume_project" {

  name        = "aws_iam_policy_for_terraform_resume_project_policy"
  path        = "/"
  description = "AWS IAM Policy for managing the resume project role"
    policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Action" : [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource" : "arn:aws:logs:*:*:*",
          "Effect" : "Allow"
        },
        {
          "Effect" : "Allow",
          "Action" : [
            "dynamodb:UpdateItem",
			      "dynamodb:GetItem"
          ],
          "Resource" : "arn:aws:dynamodb:*:*:table/VisitorCountTable"
        },
      ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
  role = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.iam_policy_for_resume_project.arn
}

# Reference the location of Lambda function
data "archive_file" "zip" {
    type = "zip"
    source_dir = "${path.module}/lambda/"
    output_path = "${path.module}/packedLambda.zip"
}

resource "aws_lambda_function_url" "url1" {
  function_name = aws_lambda_function.myLambdaFunction.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = true
    allow_origins = ["*"]
    allow_methods = ["*"]
    allow_headers = ["date", "keep-alive"] 
    expose_headers = ["keep-alive", "date"]
    max_age = 86400
  }
}