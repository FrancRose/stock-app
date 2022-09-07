from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_call = requests.get("https://cloud.iexapis.com/stable/stock/" +  ticker + "/quote?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")

        try:
            api = json.loads(api_call.content)
        except Exception as e:
            api = "ERROR"
        return render(request, 'index.html', {'api': api})

    else:
        return render(request, 'index.html', {'ticker': "Enter a Ticker Symbol in the search box above"})


    

def about(request):
    return render(request, 'about.html', {})