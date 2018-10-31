import boto3
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def new_note(request):
    return render(request, 'new_note.html')

def add_note(request):
    create_note(request)
    return render(request, 'add_note.html')

def notes(request):
    return render(request, 'notes.html')

def create_note(request):
    name = request.POST['name']
    note_text = request.POST['note']
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    note = {
        'name': {
            'S': name
        },
        'note': {
            'S': note_text
        }
    }
    response = dynamodb.put_item(
        TableName='doctors_note',
        Item=note
    )
