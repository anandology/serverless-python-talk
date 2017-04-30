# Serverless Computing with Python

---

# Who is speaking?

![right](https://pipal.in/media/trainers/anand.jpeg)

Anand Chitipothu
@anandology

- advanced programming courses at @pipalacademy
- building a data science platform at @rorodata

---

# Agenda

- Understanding serverless computation
- Available serverless platforms
- Tools in the python ecosystem
- Event driven programming
- Couple of demos

---

# What is serverless?

- function as basic compute unit
- no servers to manage
- auto scaled
- pay for use

No need to worry about managing servers and scaling.

---

# Available platforms

- AWS Lambda - supports Python 2.7 and Python 3.6 (newly added)
- Google Cloud Functions - Python 2.7, Python 3 can be supported using docker
- Azure Functions - Not sure
- IBM Open Whisk - docker support

I'm going to focus only on AWS Lambda.

---

# How does it work?

For every function invocation:

- start a new container with the application code
- Invokes the function
- responds back with the result

---

# What is the big deal?

Shared economy at its best!

Serverless is Uber of compute resources.

---

# What about webapps?

A Python webapp is WSGI function!

```
[WSGI Function] <- [AWS Lambda] <- [API Gateway]
```

---

# What else we can do?

Event-driven programming!

Trigger functions on various events.

For example, trigger a resize function whenever an image is uploaded to an S3 bucket.

---

# How to create a lambda function?

	aws lambda create-function \
		--function-name add \
		--handler add.add 	\
		--runtime python2.7	\
		--zip-file fileb://add.zip \
		--region us-east-1 	\
		--role arn:aws:iam::404682499200:role/basic_lambda_role 

You must create an AWS IAM role before creating a lambda function. The code and required libraries and binaries must to zipped and uploaded.

---

# How to invoke a function?

	aws lambda invoke \
		--invocation-type RequestResponse \
		--function-name add \
		--region us-east-1 	\
		--log-type Tail 	\
		--payload '{"a":1, "b":2 }' \
		outputfile.txt

---

# Any tools to simplify this?

Zappa - <https://www.zappa.io/>

It takes care of:

* creating zip file
* creating a lambda function
* linking it to AWS gateway
* provisioning multiple environments (dev, prod, testing)
* versioning and rollback support

---

# Demo

---

# Questions?

Anand Chitipothu
@anandology

<https://github.com/anandology/serverless-python-talk>
