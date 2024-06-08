# First, list all parameters
awslocal ssm describe-parameters --output text --query "Parameters[*].Name" | while read -r name; do
  # Then delete each parameter
  awslocal ssm delete-parameter --name "$name"
done
