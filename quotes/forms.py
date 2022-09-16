from django import forms
from django .forms import ModelForm
from .models import Stock
from .models import Trade

class StockForm(forms.ModelForm):
    class Meta: 
        model = Stock
        fields = ["stonks"]

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = ["symbol", "qty"]
