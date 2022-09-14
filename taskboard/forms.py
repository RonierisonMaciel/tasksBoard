from django import forms
from .models import Task, Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["board_id", "title", "description", "status"]


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["id", "status"]
