from django import forms
from boards.models import Board, Task
from .widgets import XDSoftDateTimePickerInput

class TaskForm(forms.Form):
    name = forms.CharField()
    points = forms.IntegerField(min_value = 1)
    board_id = forms.CharField()

    date = forms.DateField(
    input_formats=['%m/%d/%Y'],
    required = False,
    widget=XDSoftDateTimePickerInput())


class WorkForm(forms.Form):
    points = forms.IntegerField(min_value = 0)
    task_id = forms.CharField()

class BoardForm(forms.Form):
    name = forms.CharField()
    user_id = forms.CharField()
    use_due_date = forms.BooleanField(required = False)

class BoardDelete(forms.Form):
    board_id = forms.CharField()

class ScrumForm(forms.Form):
    task_ids = forms.CharField()
