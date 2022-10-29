from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def end(request):
    return render(request, 'endpoint/end.html')


def task1(request):
    slackUsername = 'Stephen Doamekpor'
    age= int(25)
    bio = 'Web developer, Python developer'
    data_set = {'slackUsername': slackUsername, 'backend': True, 'age': age, 'bio': bio}
    json_dump = json.dumps(data_set)
    #return render(request, 'endpoint/task1.html', {'data_set': json_dump})
    return HttpResponse(json_dump)
