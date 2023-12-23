from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from .restapis import get_dealers_from_cf

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request): 
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
        if user is not None:
            login(request, user)    
    return render(request, 'djangoapp/about.html', context)
                

# Create a `logout_request` view to handle sign out request
def logout_request(request): 
    context = {}
    if request.method == "POST":
        logout(request)
    return render(request, 'djangoapp/about.html', context)

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["psw"]
        f = request.POST["fname"]
        l = request.POST["lname"]
        user = User.objects.create_user(username=u, password=p, first_name=f, last_name=l)
        user.save()
        login(request, user)
        return render(request, 'djangoapp/about.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "https://e6fa4ee5-230b-4d66-9a21-15df29d6a089-bluemix.cloudantnosqldb.appdomain.cloud/dealerships/dealer-get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

