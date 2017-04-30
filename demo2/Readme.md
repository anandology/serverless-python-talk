# Demo of deploying a python webapp using Zappa

First create a virtualenv.

	$ virtualenv venv
	...
	
	$ source activate venv/bin/activate

Install required python packages.

	$ pip install -r requirements.txt

Initialize the zappa project.

	$ zappa init
	Welcome to Zappa!
	...
	What do you want to call this environment (default 'dev'): dev
	If you don't have a bucket yet, we'll create one for you too.
	What do you want call your bucket? (default 'zappa-5how7espc'):

	What's the modular path to your app's function?
	This will likely be something like 'your_module.app'.
	Where is your app's function?: hello.application

	You can optionally deploy to all available regions in order to provide fast global service.
	If you are using Zappa for the first time, you probably don't want to do this!
	Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]: n

	Okay, here's your zappa_settings.js:

	{
	    "dev": {
	        "app_function": "hello.application",
	        "aws_region": "us-east-1",
	        "profile_name": "default",
	        "s3_bucket": "zappa-5how7espc"
	    }
	}

Deploy the application.

	$ zappa deploy dev
	...
	Deployment complete!: https://r8a3qfwf13.execute-api.us-east-1.amazonaws.com/dev	

Once it is deploy, for subsequent changes:

	$ zappa update dev

