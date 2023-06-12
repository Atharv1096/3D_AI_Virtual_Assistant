from django.shortcuts import render

# Create your views here.
import sys
import os

# Get the path to the 'project_codes' folder
project_codes_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'project_codes'))

# Add the 'project_codes' path to the Python path
sys.path.insert(0, project_codes_path)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from .project_codes.Google_speech_to_text import transcribe
from .project_codes.text_to_speech import text_to_speech
from .project_codes.google_module import *
from .project_codes.youtube_module import *
from .project_codes.mathematics_module import *
from .project_codes.Google_maps import *


@csrf_exempt
def schedule(request):
    if request.method == 'POST':
        data_txt = request.POST.get('data')

        if not data_txt:
            return JsonResponse({'error': 'No data provided'})

        output = schedular(data_txt)

        if not output:
            return JsonResponse({'input': data_txt, 'response': "Sorry, but I can't find an answer for that"})

        # text_to_speech(output)  # If you want to convert the output to speech

        return JsonResponse({'input': data_txt, 'response': output})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def schedular(data):
    resmy = [int(i) for i in data.split() if i.lstrip("-").isdigit()]

    output = ""

    if len(resmy) > 0:
        output = Mathematics(myinput=data, resmy=resmy)
    elif "cast" in data or "members" in data:
        output = gscraperlist(original_data=data)
        if (output == ""):
            output = gscraper(original_data=data)
    elif "companies" in data or "startups" in data:
        output = gscraperlist(original_data=data)
        if (output == ""):
            output = gscraper(original_data=data)
    elif "video" in data or "play" in data:
        output = youtube(data=data)
    elif "distance" in data:
        output = google_maps_func(data=data)
    elif "open" in data and "video" not in data:
        output = google_open(original_data=data)
    else:
        output = gscraper(original_data=data)  # call chatgpt in gscraper

    return output
