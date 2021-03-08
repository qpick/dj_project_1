from django import forms


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Please enter Entry title",
                            widget=forms.TextInput(attrs={'class': 'form-control col-md-6 col-lg-6'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-6 col-lg-6', 'rows': 10}))
