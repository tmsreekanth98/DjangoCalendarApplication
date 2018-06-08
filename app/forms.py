from django import forms


class EntryForm(forms.Form):
    name=forms.CharField()
    date=forms.DateTimeField()
    description=forms.CharField(widget=forms.Textarea)