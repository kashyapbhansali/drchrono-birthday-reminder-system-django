from django import forms

# forms go here
class birthdayEmailForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
