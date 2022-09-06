from django.shortcuts import render

def home(request):
    import requests
    import json

    #pk_7da063ed32a0479b93e5e2e9cd6d7619 API Key
    api_call = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")

    try:
        api = json.loads(api_call.content)
    except Exception as e:
        api = "ERROR"

    return render(request, 'index.html', {'api' : api})

def about(request):
    return render(request, 'about.html', {})