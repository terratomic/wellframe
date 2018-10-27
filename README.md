# Wellframe Challenge

## To install and run
Make sure you have docker-compose installed.
```
git clone https://github.com/terratomic/wellframe.git
cd wellframe
docker-compose build
docker-compose up
```

## APIs
I like to use Postman to execute API calls with JSON data

Alternatively, Django offers automatic browsable API interfaces which allow you to send parameters via HTML form input (http://localhost:8000/api/patients). The POST method in the Patient Medication API doesn't work well with this form input - please switch to sending parameters via the JSON objects in Raw data tab.

### Medications API: /api/medications
##### GET
all: /api/medications\
one: /api/medications/{medication_id}
##### POST
/api/medications

JSON body\
{"name":"Advil"}

##### DELETE
/api/medications/id

### Patients API: /api/patients
##### GET
all: /api/patients\
one: /api/patients/id
##### POST
/api/patients

JSON body\
{\
  "name":"Hettie",\
  "medications":[1,3,5]\
}
##### DELETE
/api/patients/{patient_id}

### Patient Medication API: /api/patient/{patient_id}/medications
##### GET:
/api/patient/{patient_id}/medications
##### POST:
/api/patient/{patient_id}/medications

JSON body\
{\
  "ids":[1,3,5]\
}
##### DELETE:
/api/patient/{patient_id}/medications/{medication_id}

## Sample flow

#### Add a few medications

POST /api/medications

{"name":"Robitussin"}\
{"name":"Advil"}\
{"name":"Tylenol"}\
{"name":"Sudafed"}\
{"name":"Benadryl"}

#### Look at all the meds

GET /api/medications

#### Look more closely at one of them

GET /api/medications/1

#### Decide you want to delete it (maybe Robitussin is not your cup of tea)
DELETE /api/medications/1

#### Double check to make sure you deleted it (I hated Robitussin as a kid. I get it.)
GET /api/medications

#### Now add a few patients
POST /api/patients

{\
  "name":"Dracula",\
  "medications":[]\
}\
{\
  "name":"Hulk",\
  "medications":[3]\
}\
{\
  "name":"Malfoy",\
  "medications":[2,4]\
}

#### Feel free to look at your patients more or delete ones you aren't fond of
GET /api/patients\
GET /api/patients/1\
DELETE /api/patients/1

#### We'll move on to looking at our patients' medications, starting with Malfoy.
GET /api/patients/3/medications

#### Let's prescribe more medicine to him.
POST /api/patients/3/medications

{\
  "ids":[3,5]\
}

#### Finally, we realize we accidentally prescribed a medicine and want to remove it.
DELETE /api/patients/3/medications/2
