# from contextlib import redirect_stderr
# from email import message

from calendar import calendar
import datetime
from django.shortcuts import render, redirect
from .models import Stock
from .models import Trade
from .forms import StockForm
from .forms import TradeForm
from django.contrib import messages

def home(request):
    import alpaca_trade_api as trader
    import requests
    import json

    API_KEY = "PKT4ENR9VZAGSL1U8SY5"
    API_SECRET = "dOVfXJolecFXd5jFeLtAAJ4hp7FCDk6mkOW17ScE"
    BASE_URL = "https://paper-api.alpaca.markets"
    alpaca = trader.REST(API_KEY, API_SECRET, BASE_URL)

    clock = alpaca.get_clock()

    if request.method == 'POST':
        ticker = request.POST['ticker_symbol']
        api_call = requests.get("https://cloud.iexapis.com/stable/stock/" +  ticker + "/quote?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")
        logo_call = requests.get("https://cloud.iexapis.com/stable/stock/" +  ticker + "/logo?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")
        news_call = requests.get("https://cloud.iexapis.com/stable/stock/" +  ticker + "/news/last/10?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")

        try:
            api = json.loads(api_call.content)
            logo = json.loads(logo_call.content)
            news = json.loads(news_call.content)
        except Exception as e:
            api = "API ERROR"
            logo = "LOGO ERROR"
            news = "NEWS ERROR"
        return render(request, 'index.html', {'api': api, 'logo': logo, 'news': news, })


    else:
        return render(request, 'index.html', {'ticker': "Enter a Ticker Symbol in the search box above", 'clock': clock})

def trade(request):
    import alpaca_trade_api as trader
    import requests
    import json
    
    API_KEY = "PKT4ENR9VZAGSL1U8SY5"
    API_SECRET = "dOVfXJolecFXd5jFeLtAAJ4hp7FCDk6mkOW17ScE"
    BASE_URL = "https://paper-api.alpaca.markets"
    alpaca = trader.REST(API_KEY, API_SECRET, BASE_URL)

    order_history = alpaca.list_orders()

    # if request.method == "POST":
    #     form = TradeForm(request.POST or None)

    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, ("Trade Submitted"))
    #         return redirect('trade')
    # else:
    #     trades = Trade.objects.all()
    #     return render(request, 'trade.html', {'trades': trades, 'order_history': order_history})
    
    if request.method == "POST":
        form = TradeForm(request.POST or None)
        symbol = request.POST['symbol']
        qty = request.POST['qty']

        if form.is_valid():
            form.save()
            messages.success(request, ("Trade Submitted"))
            return redirect('trade')
            
    else:
        trades = Trade.objects.all()
        output = []

        for api_trade in trades:
            # order = alpaca.submit_order(api_trade.symbol, api_trade.qty)
            # quote = alpaca.get_latest_quote(api_trade.symbol)

            try:
                api = json.loads(order.content)
                output.append(api)
            except Exception as e:
                api = "TRADE ERROR"

        return render(request, 'trade.html', {'trades': trades, 'output': output, 'api_trade': api_trade, 'order_history': order_history,})

def remove_trade(request, trade_id):
    item = Trade.objects.get(pk=trade_id)
    item.delete()
    messages.success(request, ("Trade has been removed"))
    return redirect(trade)

def about(request):
    import alpaca_trade_api as trader
    import requests
    import json

    API_KEY = "PKT4ENR9VZAGSL1U8SY5"
    API_SECRET = "dOVfXJolecFXd5jFeLtAAJ4hp7FCDk6mkOW17ScE"
    BASE_URL = "https://paper-api.alpaca.markets"
    alpaca = trader.REST(API_KEY, API_SECRET, BASE_URL)

    account_call = alpaca.get_account()
    positions = alpaca.list_positions()
    clock = alpaca.get_clock()
    calendar = alpaca.get_calendar(start='2022-09-01', end=datetime.datetime.now() )
    history = alpaca.get_portfolio_history()
    orders = alpaca.list_orders()

    return render(request, 'about.html', {'account_call': account_call, 'positions': positions,"clock": clock, "calendar": calendar, "history": history, "orders": orders,})

def add_stock(request):
    import requests
    import json

    if request.method =='POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Is Being Tracked"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []

        for ticker_item in ticker:
            api_call = requests.get("https://cloud.iexapis.com/stable/stock/" +  str(ticker_item) + "/quote?token=pk_7da063ed32a0479b93e5e2e9cd6d7619")

            try:
                api = json.loads(api_call.content)
                output.append(api)
            except Exception as e:
                api = "ERROR"
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock had been deleted"))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})