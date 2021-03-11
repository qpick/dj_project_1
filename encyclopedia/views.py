import random

from django.shortcuts import render, redirect

from . import util
from encyclopedia import forms as app_forms
from .util import _markdown_to_html_converter as md_converter


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })


def entry_detail(request, entry):
    get_entry = util.get_entry(entry)

    if not get_entry:
        return render(request, 'encyclopedia/entry_does_not_exists.html', {'entry': entry})

    entry_title = entry
    entry = md_converter(get_entry)
    return render(request, 'encyclopedia/entry_detail.html', {'entry': entry, 'entry_title': entry_title})


def new_entry(request):
    form = app_forms.NewEntryForm()

    return render(request, 'encyclopedia/new_entry.html', {
        'form': form
    })


def edit_entry(request, title):
    entry = util.get_entry(title)
    if not entry:
        return redirect('index')

    form = app_forms.EditEntryForm(content=entry)

    return render(request, 'encyclopedia/edit_entry.html', {
        'form': form,
        'title': title,
    })


def save_entry(request):
    if not request.method == 'POST':
        return redirect('index')

    form = app_forms.NewEntryForm(request.POST)

    if not form.is_valid():
        return redirect('index')

    title = form.cleaned_data['title']
    content = form.cleaned_data['content']

    if util.get_entry(title):
        context = {
            'message': f'Entry with title "{title}" already exists!',
            'form': form,
        }
        return render(request, 'encyclopedia/new_entry.html', context)

    util.save_entry(title, content)
    return redirect('entry_detail', entry=title)


def update_entry(request, title):
    if not request.method == 'POST':
        return redirect('index')

    form = app_forms.EditEntryForm(request.POST)

    if not form.is_valid():
        return redirect('index')

    content = form.cleaned_data['content']
    try:
        util.save_entry(title, content)
    except Exception as e:
        assert e
        return redirect('index')

    return redirect('entry_detail', entry=title)


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
        entry = md_converter(get_entry)
        return render(request, 'encyclopedia/entry_detail.html', {'entry': entry, 'entry_title': search})
