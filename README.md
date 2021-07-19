# HEALTHAPI
This is a REST API REST API that helps estimate a woman’s period cycles within a specific timeframe
# Getting Started
To run this application locally:
- Open up terminal (on MacOS) and switch directory to Desktop by running:
```
cd ~
```
- For Windows, open git bash and switch directory to Desktop by running:
```
cd Desktop
```
- Clone the repository by running:
```
git clone https://github.com/Ladeologun/HEALTHAPI.git
```
- Then run the following commands consecutively
```
cd HEALTHAPI 
```
```
python3 -m venv venv
```
- To activate virtual environment (MacOS users): 
```
source venv/bin/activate
```
- To activate virtual environment (Windows users):
```
source venv/Source/activate
```
- Install dependencies as follows (both MacOS & Windows):
```
pip3 install -r requirements.txt
```
- To run unit tests, run the command below:
```
python3 manage.py test
```
- Make migrations by running the commands below in succession:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
- To start the Django server, run:
```
python3 manage.py runserver
```
- The API endpoints are now available to be used
## Registration
- Open Postman and register a user for by making a `POST` request to the address below and with a payload in json format. A sample has been provided below

**Endpoint**

```
 http://127.0.0.1:8000/womens-health/api/register/
```
**Payload**

```
{
    "email":"kaihavertz100@gmail.com",
    "fullname":"kai havertz",
    "mobile_number":"07060165309",
    "password":"adegbenro23.",
    "age":23
}
```
- A response containing the details of the user will be received to confirm registration 

**Response**
```
{
    "email":"kaihavertz100@gmail.com",
    "fullname":"kai havertz",
    "mobile_number":"07060165309",
    "age":23
}
```
## Login

- The registered user can login by making another `POST` request to the address below and with a payload (email & password) in json format. A sample also has been provided below

**Endpoint**
```
 http://127.0.0.1:8000/womens-health/api/login/
```
**Payload**
```
{
    "email":"kaihavertz100@gmail.com",
    "password":"adegbenro23."
}
```
- A response containing a success message and generated **token** to authorize the user to make further requests

**Response**
```
{
    "message": "success",
    "token": <random_generated_token>
}
```

## Creation of Cycle (Authorization)
- The registered user can create a cycle by making a `POST` request to the address below and with a payload in json format. A sample also has been provided below
- Note: This endpoint requires `Token Authentication`. The generated token in the `LOGIN` endpoint can be passed into the headers in the format also described below

**Endpoint**
```
http://127.0.0.1:8000/womens-health/api/create-cycles/
```
**Headers**
```
"Authorization" : "Token <generated_token>"
```
**Payload**
```
{
    "Last_period_date":"2020-06-20",
    "Cycle_average":25,
    "Period_average": 5,
    "Start_date":"2020-07-25",
    "End_date":"2021-07-25"
}
```
- A response containing the name of the user and `total_created_cycles` will be received.
- Expected result has been displayed below

**Response**
```
{
    "name": "kai havertz",
    "total_created_cycles": 15
}
```
## Updating of Cycle (Authorization)
- The registered user can create a cycle by making a `PUT` request to the address below and with a payload in json format which will update user information. A sample also has been provided below
- Note: This endpoint also requires `Token Authentication`. The generated token in the `LOGIN` endpoint needs to be passed into the headers in the format also described below

**Endpoint**
```
http://127.0.0.1:8000/womens-health/api/create-cycles/
```
**Headers**
```
"Authorization" : "Token <generated_token>"
```
**Payload**
```
{
    "Last_period_date":"2020-06-20",
    "Cycle_average":25,
    "Period_average": 7,
    "Start_date":"2020-07-25",
    "End_date":"2021-08-25"
}
```
- A response containing the name of the user and `total_created_cycles` will be received.
- Expected result has been displayed below

**Response**
```
{
    "name": "kai havertz",
    "total_created_cycles": 16
}
```
## Listing of Cycle Events (Authorization)
- The registered user can view their current cycle events by making a `GET` request to the address below and without any payload. However, a path parameter (date) needs to be provided in the url. An example has been provided below
- Note: This endpoint also requires `Token Authentication`. The generated token in the `LOGIN` endpoint needs to be passed into the headers in the format also described below

**Endpoint**
```
http://127.0.0.1:8000/women-healths/api/cycle-event/?date=2021-01-05
```
**Headers**
```
"Authorization" : "Token <generated_token>"
```
- A response containing the `event` and the `date` will be received.
- Expected result has been displayed below

**Response**
```
{
    "event": "post_ovulation_window",
    "date": "2021-01-05"
}
```
