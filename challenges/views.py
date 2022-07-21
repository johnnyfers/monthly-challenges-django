from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

monthly_challenges_dict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def index(request):
    months = list(monthly_challenges_dict.keys())
    
    return render(request,'challenges/index.html', {
        'months': months
    })


def monthly_challenges_by_number(_request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid')

    forward_month = months[month-1]
    redirect_path = reverse('month_challenges', args=[forward_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        print('asdsad', challenge_text)
        
        return render(request, 'challenges/challenge.html', {
            'challenge_text': challenge_text,
            'month': month.capitalize()
            })
    except KeyError as e:
        print(e)
        raise Http404()
