from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import minutesForm


def index(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')


# @login_required(login_url='login_page')
def minute_form(request):
    if request.method == 'POST':
        form = minutesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Record was successfully added to the database!')
        # return HttpResponseRedirect('/company_form')
    else:
        form = minutesForm()
    return render(request, 'minute_form.html', {'form': form})
