from django import forms
from django.forms import ModelForm, Select
from .models import Food

class CalcuFilter(ModelForm):

    CATEGORIES = (
        ('ALL', 'ANY'),
        ('CHI', 'CHICKEN'),
        ('BUR', 'BURGER')
    )

    category = forms.ChoiceField(choices=CATEGORIES, required=False)


    class Meta:
        model = Food
        fields = ['pro', 'category']
        labels = {
            'pro': 'How many grams of protein do you need?   ',
        }