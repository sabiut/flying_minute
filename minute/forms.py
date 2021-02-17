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
        fields = '__all__'
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
