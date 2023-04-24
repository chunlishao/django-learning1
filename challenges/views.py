from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthMapping = {1 : "january", 
                2 : "feburary",
                3 : "march",
                4 : "april"}

monthChallenges = {"january" : "run every day",
                   "feburary" : "learning coding",
                   "march" : "be focus",
                   "april" : "find a job",}

redirect_basic_url = "month_challenge"

def GoHome(request):
    months = list(monthChallenges.keys())
    list_item = ""

    for month in months:        
        redirect_path = reverse(redirect_basic_url, args=[month])
        list_item += f"<li><a href=\"{redirect_path}\">{month}</a></li>"

    return HttpResponse(f"<ul>{list_item}</ul>")

def indexByNum(request, month):
    if monthMapping.__contains__(month):
        redirect_month = monthMapping[month]
        redirect_path = reverse(redirect_basic_url, args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("not valid")
    
    
def index(request, month):
    try:
        respondData = f"<h1>{monthChallenges[month]}</h1>"
        return HttpResponse(respondData)
    except:
        return HttpResponseNotFound("this month is not supported")
    