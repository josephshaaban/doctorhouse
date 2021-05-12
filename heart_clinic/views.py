from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from heart_clinic.models import Article


def index(request):
    articles = Article.objects.all().order_by('visit_count')
    print(articles[0].image.url)
    content = dict(
        articles=articles,
    )
    return render(request, 'index.html', context=content)


def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except ObjectDoesNotExist:
        return HttpResponse(content='404 Not found')
    except MultipleObjectsReturned:
        return HttpResponse(content='404 Not found')
    article.visit_count = article.visit_count + 1
    article.save()
    context = dict(
        article=article,
    )
    return render(request, 'article_page.html', context=context)


def heart_clinic(request):
    context = dict(
    )
    return render(request, 'heart_clinic_home.html', context=context)
