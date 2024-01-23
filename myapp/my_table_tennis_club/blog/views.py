from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Blog


# Create your views here.
def blog(request):
    blog = Blog.objects.all().values()
    template = loader.get_template('all-blogs.html')

    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'blog': blog,
    }

    return HttpResponse(template.render(context, request))
