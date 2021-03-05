from django.shortcuts import render
from markdown2 import markdown
from . import util
from django import forms


class NewEntryForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })


def entry_detail(request, entry):
    return render(request, 'encyclopedia/entry_detail.html', {
        'entry': markdown(util.get_entry(entry))
    })


def new_entry(request):
    form = NewEntryForm()
    return render(request, 'encyclopedia/new_entry.html', {
        'form': form
    })


def save_entry(request):
    pass


def edit_entry(request):
    pass


def random_entry(request):
    pass


def search_entry(request):
    pass
