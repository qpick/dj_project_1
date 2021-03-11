from django import forms


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Please enter Entry title",
                            widget=forms.TextInput(attrs={'class': 'form-control col-md-6 col-lg-6'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-6 col-lg-6', 'rows': 25}))


class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-6 col-lg-6', 'rows': 25}))

    def get_initial_for_field(self, field, field_name):
        if field_name == 'content':
            return self.content
        return super().get_initial_for_field(field, field_name)

    def __init__(self, *args, **kwargs):
        try:
            self.content = kwargs.get('content')
            kwargs.pop('content')
        except Exception as e:
            assert e

        super().__init__(*args, **kwargs)
