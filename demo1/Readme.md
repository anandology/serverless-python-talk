# Creating AWS Lambda by hand

Derived from:
https://medium.com/@jacobsteeves/aws-lambda-from-the-command-line-7efab7f3ebd9


---
```
$ cat basic_lambda_role.json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": { "AWS" : "*" },
        "Action": "sts:AssumeRole"
    }]
}

$ aws iam create-role --role-name basic_lambda_role --assume-role-policy-document file://basic_lambda_role.json
{
    "Role": {
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "*"
                    }
                }
            ]
        },
        "RoleId": "AROAISB4IF7IJ36RF3YQW",
        "CreateDate": "2017-04-30T04:24:42.259Z",
        "RoleName": "basic_lambda_role",
        "Path": "/",
        "Arn": "arn:aws:iam::404682499200:role/basic_lambda_role"
    }
}

$ cat add.py

def add(event, context):
    return event['a'] + event['b']

$ zip add.zip add.py
  adding: add.py (deflated 15%)


$ aws lambda create-function --region us-east-1 --function-name add --zip-file fileb://add.zip --role arn:aws:iam::404682499200:role/basic_lambda_role --handler add.add --runtime python2.7
{
    "CodeSha256": "kJzldJ/ZwwiBYLrsKQ6lAtg3hJcjAYUTILGZspQ4AVA=",
    "FunctionName": "add",
    "CodeSize": 214,
    "MemorySize": 128,
    "FunctionArn": "arn:aws:lambda:us-east-1:404682499200:function:add",
    "Version": "$LATEST",
    "Role": "arn:aws:iam::404682499200:role/basic_lambda_role",
    "Timeout": 3,
    "LastModified": "2017-04-30T04:29:47.023+0000",
    "Handler": "add.add",
    "Runtime": "python2.7",
    "Description": ""
}

$ aws lambda invoke \
--invocation-type RequestResponse \
--function-name add \
--region us-east-1 \
--log-type Tail \
--payload '{"a":1, "b":2 }' \
outputfile.txt

$ cat outputfile.txt
3

To see the log messages:

$ aws lambda invoke --invocation-type RequestResponse --function-name add --region us-east-1 --log-type Tail --payload '{"a":1, "b":2 }' outputfile.txt | jq -r '.LogResult' | base64 --decode

START RequestId: 8d7d02fa-2d60-11e7-9211-7fe5c5e9ad64 Version: $LATEST
END RequestId: 8d7d02fa-2d60-11e7-9211-7fe5c5e9ad64
REPORT RequestId: 8d7d02fa-2d60-11e7-9211-7fe5c5e9ad64	Duration: 0.39 ms	Billed Duration: 100 ms 	Memory Size: 128 MB	Max Memory Used: 21 MB

```

To delete the lambda function:

	$ aws lambda delete-function  --function-name add
