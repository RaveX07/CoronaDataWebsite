from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def overview(request):
    response = requests.get("https://api.corona-zahlen.org/districts")
    r_json = response.text

    data = json.loads(r_json)

    nameList = []
    incidenceList = []
    casesList = []
    deathsList = []
    stateList = []

    for x in data['data']:
        nameList.append(data['data'][x]['name'])
        incidenceList.append(data['data'][x]['weekIncidence'])
        casesList.append(data['data'][x]['cases'])
        deathsList.append(data['data'][x]['deaths'])
        stateList.append(data['data'][x]['state'])
        

