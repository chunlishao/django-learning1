from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthMapping = {1 : "january", 
                2 : "feburary",
                3 : "march",
                4 : "april"}

monthChallenges = {"january" : "run every day",
                   "feburary" : "learning coding",
                   "march" : "be focus",
                   "april" : None,}

redirect_basic_url = "month_challenge"

def GoHome(request):
    months = list(monthChallenges.keys())
    list_item = ""

    return render(request, "challenges/index.html", {
        "months" : months
    })


def indexByNum(request, month):
    redirect_month = "invalid"
    if monthMapping.__contains__(month):
        redirect_month = monthMapping[month]
    
    redirect_path = reverse(redirect_basic_url, args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
def index(request, month):
    try:
        respondData = monthChallenges[month]
        return render(request, "challenges/challenge.html", {
            "month" : month,
            "challenge" : respondData
        })
    except:
        raise Http404()
    