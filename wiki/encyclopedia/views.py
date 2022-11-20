from django.shortcuts import render
import markdown2
from . import util
import markdownify
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, page):
    if util.get_entry(page):
        body = markdown2.markdown(util.get_entry(page))
    else:
        body = "Error: page not found"
    return render(request, "encyclopedia/layout.html", {
        "page": body,
        "title": page
    })

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        
        if util.get_entry(query):
            return display(request, query)
        else:
            # find existing pages that are substring of query
            entries = util.list_entries()
            results = []
            for entry in entries:
                if query in entry:
                    results.append(entry)
             
            return render(request, 'encyclopedia/search.html', {
                'results': results
            })    
def newpage(request):
    return render(request, "encyclopedia/newpage.html", {'newpage': True})

def addpage(request):
    if request.method=="POST":
        title = request.POST.get('title').capitalize()
        body = request.POST.get('newbody')
        
        if title in util.list_entries():
            return render(request, 'encyclopedia/error.html', {'title': title
            })
        else:
            util.save_entry(title, body)
            return display(request, title)

def edit(request):
    title = request.GET.get('title')
    page = request.GET.get('page')

    return render(request, 'encyclopedia/edit.html', {
        'editbody':True,
        'page': markdownify.markdownify(page, heading_style="ATX"),
        'title':title})

def posted(request):
    title = request.POST.get('title')
    page = request.POST.get('page')
    page = markdownify.markdownify(page, heading_style="ATX")

    util.save_entry(title, page)
    return display(request, title)

def randchoice(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return display(request, title)