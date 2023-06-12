from google_module import *
from youtube_module import *
from mathematics_module import *
from Google_maps import *
from Google_speech_to_text import transcribe
from text_to_speech import text_to_speech




def schedular(data):
    resmy = [int(i) for i in data.split() if i.lstrip("-").isdigit()]

    output = ""

    if (len(resmy) > 0):
        output = Mathematics(myinput=data, resmy=resmy)
    elif "cast" in data or "members" in data:
        output = gscraperlist(original_data=data)
        if (output==""):
            output = gscraper(original_data=data)
    elif "companies" in data or "startups" in data:
        output = gscraperlist(original_data=data)
        if (output==""):
            output = gscraper(original_data=data)
    elif "video" in data or "play" in data:
        youtube(data=data)
    elif "distance" in data:
        output = google_maps_func(data=data)
    elif "open" in data and "video" not in data:
        google_open(original_data=data)
    else:
        output = gscraper(original_data=data)  # call chatgpt in gscraper
    return output
    # text_to_speech(output)

