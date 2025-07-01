from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Set 3 SMART goals and track your progress weekly.",
    "february": "Do a 14-day self-love journaling challenge.",
    "march": "Exercise for at least 20 minutes every day.",
    "april": "Try one new hobby or creative project each week.",
    "may": "Complete a 30-day mindfulness or meditation challenge.",
    "june": "Start a summer reading list and finish 2 books.",
    "july": "Learn a new skill or take an online mini-course.",
    "august": "Go tech-free for 1 hour a day and spend time outdoors.",
    "september": "Organize your workspace and adopt a study/productivity routine.",
    "october": "Do something that scares you—face one fear this month.",
    "november": "Write down one thing you're grateful for every day.",
    "december": "Reflect on the year and write a personal growth recap."
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
        
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month! Please enter a valid month number.")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(f"{redirect_path}")

def monthly_challenge(request, month):
    text = monthly_challenges.get(month, "")

    if not text:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
    return render(request, "challenges/challenge.html", {
        "month_name": month,
        "text": text
    })

    # response_data = render_to_string("challenges/challenge.html",{
    #     "text": text
    # })
    # return HttpResponse(response_data)

def home(request):
    return HttpResponse("Welcome to the Monthly Challenges App!")
