# -*- coding: utf-8 -*-
from django import forms

from .models import Cities

class CityForm (forms.ModelForm):

    class Meta:
        model = Cities
        fields = ('name',)