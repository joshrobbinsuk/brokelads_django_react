# brokelads_django_react

Rebuild of brokelads betting site (see my other repositories) with Django Rest Framework, React, Redux Toolkit, Amazon Cognito/Amplify Auth, and a Celery/Redis scheduler

# Initial setup

After cloning the project, add the following env vars in the root:

```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
MY_SECRET_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
COGNITO_CUSTOMER_USER_POOL_ID=
COGNITO_CUSTOMER_APP_CLIENT_ID=
RAPID_API_KEY=
```

You will need pipenv to run the project (https://pipenv.pypa.io/en/latest/)

You will need to register a Cognito User Pool on an AWS account. (https://aws.amazon.com/cognito/)

You will also need to register a Rapid API account (https://rapidapi.com/). Rapid API starts charging users after 100 requests a day. In this codebase, external API calls are scheduled to never reach this limit. Be careful not to change this. Rapid API calls are not related to the app's traffic, although they can be triggered at will from the admin panel.

# To run locally

## Build containers

First build all docker containers

```
docker-compose build
```

## Finally

Start the project

```
docker-compose up
```

Migrate to the db

```
docker exec blweb python manage.py migrate
```

Navigate to root/frontend and run

```
npm install
npm start
```

And you should be good to go...
