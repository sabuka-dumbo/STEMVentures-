from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def index(requst):
    return render(requst, "index.html")