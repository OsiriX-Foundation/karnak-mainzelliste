import requests
import json
import sys

#######################################################################################
#
#             arg1: external id of the patient you want to search
#             arg2: mainzelliste root url
#             arg3: mainzelliste api key
#             
#             Example to run the script : 
#                 
#             python get_pseudonym.py 002WU0YA http://localhost:8083 changeThisApiKey
#
######################################################################################

pseudonym = sys.argv[1]
root_url = sys.argv[2]
api_key = sys.argv[3] 


def get_sessionid_token():
  url = root_url+"/sessions"
  payload={}
  headers = {
    'mainzellisteApiKey': 'changeThisApiKey',
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  sessionId = response.json()['sessionId']
  return sessionId

def get_search_patient_token(sessionid_token, pseudonym, idType):
  url = root_url +"/sessions/"+sessionid_token+"/tokens"
  body_payload =  {
                    'type': 'readPatients',
                    'data': {
                      'searchIds':[
                        {
                              'idType':idType,
                              'idString':pseudonym
                        }
                      ],
                      'resultFields':['patientName', 'patientID', 'issuerOfPatientID', 'patientBirthDate', 'patientSex'],
                      'resultIds':['extid']
                    }
                  } 
  body = json.dumps(body_payload)
  headers = {
    'mainzellisteApiKey': api_key,
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=body)
  if((response.text == "No patient found with provided extid '"+pseudonym+"'!") or (response.text == "No patient found with provided pid '"+pseudonym+"'!")):
    return None
  return response

def get_patient(sessionid_token,response):
    tokenIdGetPatient = response.json()['tokenId']
    url = root_url+"/patients?tokenId=" + tokenIdGetPatient
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


patient_exist = False
sessionid_token = get_sessionid_token()
response = get_search_patient_token(sessionid_token, pseudonym, 'pid')
if(response != None):
  patient_exist = True
else:
    response = get_search_patient_token(sessionid_token, pseudonym, 'extid')
    if(response != None):
      patient_exist = True

if(patient_exist):
  response = get_patient(sessionid_token, response)
  print(response)
