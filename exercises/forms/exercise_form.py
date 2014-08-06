from django import forms


class ExerciseForm(forms.Form):
    question = forms.CharField()

