from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add a new task...',
        'class': 'border p-2 rounded w-full'
    }))