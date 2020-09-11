import markdown 

from django.shortcuts import render
from random import choice
from . import forms
from . import util

form = forms.NewSearchForm()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': form
    })


def entry_page(request, title):
    if util.get_entry(title) is None: 
        return render(request, 'encyclopedia/error404.html', {
            'message': 'Page not Found'
        })
    md = markdown.Markdown()
    return render(request, 'encyclopedia/entry.html', {
        'title': title.capitalize(),
        'content': md.convert(util.get_entry(title)),
        'form': form
    })


def search(request):
    if request.method == 'GET':
        form = forms.NewSearchForm(request.GET)
        if form.is_valid():
            entries = util.list_entries()
            title = form.cleaned_data['title']
            results = [entry for entry in entries if title.lower() in entry.lower()]
            if len(results) == 1 and results[0].lower() == title.lower(): return entry_page(request, results[0])
            else: 
                return render(request, 'encyclopedia/search_results.html', {
                    'results': results,
                    'form': form,
                    'title': title
                })

def create_new_page(request):
    if request.method == 'POST':
        new_form = forms.NewPageForm(request.POST)
        if new_form.is_valid():
            title = new_form.cleaned_data['title'].capitalize()
            content = new_form.cleaned_data['content']
            entries = [entry.lower() for entry in util.list_entries()]
            if title.lower() in entries:
                return render(request, 'encyclopedia/error_already_exists.html', {
                    'message': 'Page Already Exists'
                })
            util.save_entry(title, content)
            return entry_page(request, title)
 
    return render(request, 'encyclopedia/new.html', {
            'form': form,
            'new_form': forms.NewPageForm()
        })


def edit_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        edit_form = forms.NewEditForm(request.POST)
        if edit_form.is_valid():
            content = edit_form.cleaned_data['content'].strip()
            util.save_entry(title, content)
            return entry_page(request, title)
    
    title = request.GET.get('edit')
    return render(request, 'encyclopedia/edit.html', {
        'form': form,
        'title': title,
        'edit_form': forms.NewEditForm({'content': util.get_entry(title)})
    })


def random_page(request):
    return entry_page(request, choice(util.list_entries()))

       