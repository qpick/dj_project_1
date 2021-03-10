import random
from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from .forms import *
from .custom import *


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })


def entry_detail(request, entry):
    get_entry = util.get_entry(entry)

    if not get_entry:
        return render(request, 'encyclopedia/entry_does_not_exists.html', {'entry': entry})
    else:
        entry_title = entry
        entry = _markdown_to_html_converter(get_entry)
        return render(request, 'encyclopedia/entry_detail.html', {'entry': entry, 'entry_title': entry_title})


def new_entry(request):
    form = NewEntryForm()

    return render(request, 'encyclopedia/new_entry.html', {
        'form': form
    })


def edit_entry(request, title):
    entry = util.get_entry(title)
    if entry:
        form = NewEntryForm()
        form.fields['title'].initial = title
        form.fields["title"].widget = forms.HiddenInput()
        form.fields['content'].initial = entry

        return render(request, 'encyclopedia/edit_entry.html', {
            'form': form
        })
    else:
        return redirect('index')


def save_entry(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)

        print(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            editing = True if request.POST.get('editing') else False

            if util.get_entry(title) is None or editing:
                util.save_entry(title, content)
                return redirect('entry_detail', entry=title)
            else:
                context = {
                    'message': f'Entry with title "{title}" already exists!',
                    'form': form,
                }
                return render(request, 'encyclopedia/new_entry.html', context)
    else:
        return redirect('index')


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

    #Custom converter
    #converter = (CustomMarkdown()).convert(entry)

    converter = markdown(entry)

    return converter
