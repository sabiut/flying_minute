from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import minutesForm, BoardMembersForm, AddMemberPresentForm, commentsForm, ApprovalForm
from .models import BoardMembers, fly_minute, Comments

# signup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from calendarapp.forms import SignupForm

from calendarapp.models import Event
from calendarapp.utils import Calendar
from calendarapp.views import get_date, prev_month, next_month


def index(request):
    return render(request, 'home.html')


def dashboard(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            return render(request, 'index.html')
        else:
            return render(request, 'no_access.html')


def login_page(request):
    return render(request, 'login.html')


# log user out
def log_out(request):
    auth.logout(request)
    return render(request, 'home.html')


@login_required(login_url='login_page')
def minute_form(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            if request.method == 'POST':
                form = minutesForm(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/add_member_present_form')
            else:
                form = minutesForm()
            return render(request, 'minute_form.html', {'form': form})
        else:
            return render(request, 'no_access.html')


@login_required(login_url='login_page')
def add_member_present_form(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            if request.method == 'POST':
                form = AddMemberPresentForm(request.POST)
                if form.is_valid():
                    form.save()
                    return render(request, 'member_present_success.html')
            else:
                form = AddMemberPresentForm()
            return render(request, 'add_member_present_form.html', {'form': form})
        else:
            return render(request, 'no_access.html')


def add_board_members(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            if request.method == 'POST':
                form = BoardMembersForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return render(request, 'add_member_success.html')

            else:
                form = BoardMembersForm()
            return render(request, 'board_members.html', {'form': form})
        else:
            return render(request, 'no_access.html')


def display_board_members(request):
    in_group = User.objects.filter(groups__name="organizer")
    if request.user.is_authenticated:
        if request.user in in_group:
            board_members = BoardMembers.objects.all()
            return render(request, 'display_board.html', locals())
        else:
            return render(request, 'no_access.html')


@login_required(login_url='login_page')
def update_member_form(request, member_id):
    if request.method == 'POST':
        get_member_id = BoardMembers.objects.get(id=member_id)
        form = BoardMembersForm(request.POST, instance=get_member_id)
        if form.is_valid():
            form.save()
            # messages.info(request,'successfully updated the board record.')
            return render(request, 'success_message.html')
    else:
        get_member_id = BoardMembers.objects.get(id=member_id)
        form = BoardMembersForm(instance=get_member_id)
    return render(request, 'add_member.html', locals())


@login_required(login_url='login_page')
def drop_member(request, member_id):
    delete_member = BoardMembers.objects.get(id=member_id)
    delete_member.delete()
    return render(request, 'delete_member_success.html')


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
                if user.groups.filter(name="member").exists():

                    return HttpResponseRedirect('/member')
                else:
                    return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'signup.html', context)


# @login_required(login_url='home')
# def member_page(request):
#     username = None
#     if request.user.is_authenticated:
#         return render(request, 'member.html')


def user_logout(request):
    logout(request)
    return redirect('signup')


@login_required(login_url='login_page')
def upload_file(request):
    return render(request, 'upload_page.html')


@login_required(login_url='login_page')
def minutes(request):
    return render(request, 'minutes.html')


@login_required(login_url='login_page')
def DisplayGenetratedMinutes(request):
    board_minutes = fly_minute.objects.all()
    return render(request, 'display_generated_minutes.html', locals())


#
# @login_required(login_url='login_page')
# def MinutesReport(request, flyminute_id):
#     report = fly_minute.objects.filter(id=flyminute_id).prefetch_related('memberspresent_set')
#     context = {'report': report}
#     return render(request, 'minute_report.html', context)


@login_required(login_url='login_page')
def MinutesReport(request, flyminute_id):
    report = fly_minute.objects.filter(id=flyminute_id).prefetch_related('memberspresent_set')
    comment = fly_minute.objects.filter(id=flyminute_id).prefetch_related('comments')
    reportest = fly_minute.objects.filter(id=flyminute_id).prefetch_related('memberspresent_set')
    return render(request, 'minute_report.html', locals())


@login_required(login_url='login_page')
def display_report(request, report_id):
    report = fly_minute.objects.filter(id=report_id).prefetch_related('memberspresent_set')
    context = {'report': report}
    return render(request, 'report.html', context)


@login_required(login_url='login_page')
def display_comment(self, request):
    comment = Comments.objects.filter(comment=self.report).order_by("date_created")


@login_required(login_url='login_page')
def commentForm(request):
    if request.method == 'POST':
        form = commentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/DisplayGenetratedMinutes')
            # return render(request, 'comment_added_successfully.html')

    else:
        form = commentsForm()
    return render(request, 'newComment.html', {'form': form})


@login_required(login_url='login_page')
def update_fly_minute_form(request, minutes_id):
    if request.method == 'POST':
        get_minute_id = fly_minute.objects.get(id=minutes_id)
        form = minutesForm(request.POST, instance=get_minute_id)
        if form.is_valid():
            form.save()
            # messages.info(request,'successfully updated the board record.')
            return render(request, 'fly_minute_success_message.html')
    else:
        get_member_id = fly_minute.objects.get(id=minutes_id)
        form = minutesForm(instance=get_member_id)
    return render(request, 'add_member.html', locals())



@login_required(login_url='login_page')
def authorize_minute_form(request, auth_minutes_id):
    if request.method == 'POST':
        get_minute_id = fly_minute.objects.get(id=auth_minutes_id)
        form = ApprovalForm(request.POST, instance=get_minute_id)
        if form.is_valid():
            form.save()
            # messages.info(request,'successfully updated the board record.')
            return render(request, 'fly_minute_success_message.html')
    else:
        get_minute_id = fly_minute.objects.get(id=auth_minutes_id)
        form = ApprovalForm(instance=get_minute_id)
    return render(request, 'authorize_minute.html', locals())
