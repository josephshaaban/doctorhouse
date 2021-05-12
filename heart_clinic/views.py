from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from heart_clinic.models import Article


def index(request):
    """ helper method to get the version information into the top-view """
    articles = Article.objects.all()
    print(articles[0].image.url)
    content = dict(
        articles=articles,
    )
    return render(request, 'index.html', context=content)


def heart_clinic(request):
    content = dict(
    )
    return render(request, 'heart_clinic_home.html', context=content)
