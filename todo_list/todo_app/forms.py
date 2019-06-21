from django import forms
from .models import todo_list
class listform(forms.ModelForm):
    Title=forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder': 'todo title'}))
    Description=forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder': 'description'}))
    DateTime_of_todo_task=forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd hh:mm:ss'}))
    class Meta:
        model=todo_list
        fields='__all__'
