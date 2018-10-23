# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here
def index(request):
    context = {'message': 'i'}
    return render(request, 'webapp/index.html', context)


def taizhang(request):
    return render(request, 'webapp/taizhang.html')