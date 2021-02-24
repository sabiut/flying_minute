from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .forms import minutesForm, BoardMembersForm
from .models import BoardMembers

# signup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from calendarapp.forms import SignupForm


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


def add_board_members(request):
    if request.method == 'POST':
        form = BoardMembersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Record was successfully added to the database!')
        # return HttpResponseRedirect('/company_form')
    else:
        form = BoardMembersForm()
    return render(request, 'board_members.html', {'form': form})


def display_board_members(request):
    board_members = BoardMembers.objects.all()
    return render(request, 'display_board.html', locals())


def signup(request):
    forms = SignupForm()
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return redirect('signup')
