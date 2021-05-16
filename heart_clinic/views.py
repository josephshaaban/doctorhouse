from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.views import View

from doctorhouse import settings
from heart_clinic.forms import HeartConsultationForm, HeartConsultationSystemForm
from heart_clinic.helpers.id3 import calculate
from heart_clinic.models import Article, HeartConsultation

import pandas as pd


def index(request):
    articles = Article.objects.all().order_by('-visit_count')
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HeartConsultationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HeartConsultationForm()

    context = dict(
        form=form,
    )
    return render(request, 'heart_clinic_home.html', context=context)


class SendEmail(View):
    def post(self, request, *args, **kwargs):
        consultation = get_object_or_404(HeartConsultation, pk=self.kwargs['pk'])
        response_email = {
            'subject': 'Heart Consultation response',
            'body': f"Dear {consultation.full_name},\n\n{request.POST['response']}\n\nThanks!",
            'from': 'youssef.shaaban.995@gmail.com',
            'recipient_list': [consultation.email],
        }

        send_mail(
            response_email['subject'],
            response_email['body'],
            settings.EMAIL_HOST_USER,
            response_email['recipient_list'],
            fail_silently=False
        )
        messages.add_message(request, messages.INFO, 'The email sent successfully!')
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


def thanks(request):
    context = dict(
    )
    return render(request, 'thanks.html', context=context)


def heart_adm_system(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HeartConsultationSystemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = list(form.cleaned_data.values())
            data = [data]
            df = pd.DataFrame(
                data=data,
                columns=form.cleaned_data.keys()
            )
            y_pred = calculate(excel_file='heart_disease_male.xls', test_data=df)[0]

            consultation = form.save(commit=False)
            consultation.disease = y_pred
            consultation.save()

            context = dict(
                y_pred=y_pred,
            )
            return render(request, 'thanks.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HeartConsultationSystemForm()

    context = dict(
        form=form,
    )
    return render(request, 'heart_adm_system.html', context=context)
