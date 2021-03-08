import random
from django import forms
from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util



class NewEntryForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())


def index(request):

    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })


def entry_detail(request, entry):
    get_entry = util.get_entry(entry)

    if not get_entry:
        return render(request, 'encyclopedia/entry_does_not_exists.html', {'entry': entry})
    else:
        entry = _markdown_to_html_converter(get_entry)
        return render(request, 'encyclopedia/entry_detail.html', {'entry': entry})


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
    entries = util.list_entries()
    find_random_entry = random.choice(entries)

    return redirect('entry_detail', entry=find_random_entry)


def search_entry(request):
    search = request.GET.get('q').strip()
    get_entry = util.get_entry(search)

    if not get_entry:
        entries = util.list_entries()

        get_similar_entries = []
        for entry in entries:
            if search.lower() in entry.lower():
                get_similar_entries.append(entry)

        return render(request, 'encyclopedia/index.html', {'entries': get_similar_entries})
    else:
        entry = _markdown_to_html_converter(get_entry)
        return render(request, 'encyclopedia/entry_detail.html', {'entry': entry})


def _markdown_to_html_converter(entry):
    """Convert markdown to html format, return html format."""
    return markdown(entry)