from .models import *
from django import forms


# setup date picker start
class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class minutesForm(forms.ModelForm):
    class Meta:
        model = fly_minute
        fields = 'mode_of_meeting', 'date', 'Time', 'minute_prepared_by', 'location', 'authorize_by', 'item', 'owner', 'recommendations', 'notes', 'issues', 'resolutions', 'resolution_Owner', 'due_date', 'Action',
        'department_or_person_responsible'
        widgets = {
            'date': DateInput(), 'due_date': DateInput(),
            'Time': TimeInput()
        }


class approvalForm(forms.ModelForm):
    class Meta:
        model = fly_minute
        fields = 'authorize_by_chairman', 'authorize_by_director_ex_officio', 'authorize_by_directors', 'Minute_approved_by_the_Chairmen', 'Approval_date'

        widgets = {
            'Approval_date': DateInput()
        }


class BoardMembersForm(forms.ModelForm):
    class Meta:
        model = BoardMembers
        fields = '__all__'
        widgets = {
            'start_date': DateInput()
        }


class AddMemberPresentForm(forms.ModelForm):
    class Meta:
        model = MembersPresent
        fields = '__all__'
