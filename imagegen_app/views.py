
from PIL import Image
import requests
from django.http import HttpResponse
from django.shortcuts import render
from openai import OpenAI

client = OpenAI(api_key='sk-E......')


def generate_image(request):
    text_input = request.GET.get('text_input')
    image_url = None
    error_message = None
    
    if not text_input:
        error_message = "Please provide input text."
    else:
        if '\n' in text_input:
            prompt = text_input
        else:
            features_input = request.GET.get('features_input')
            if features_input is not None:
                prompt = f"{text_input}\n{features_input}"
            else:
                prompt = text_input
            
        response = client.images.generate(prompt=prompt, n=1, size='512x512')
        image_url = response.data[0].url
    
    context = {'image_url': image_url, 'error_message': error_message}
    return render(request, 'generate.html', context)
