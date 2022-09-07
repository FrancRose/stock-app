# from contextlib import redirect_stderr
# from email import message

from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker_symbol']
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

def add_stock(request):
    if request.method =='POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Is Being Tracked"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})

