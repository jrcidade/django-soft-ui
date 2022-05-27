# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import patient
from .forms import patientForm
from django.contrib import messages


#@login_required(login_url="/login/")
#def index(request):

    #create the user form
    #AuthorFormSet = modelformset_factory(patient, fields=('Firstname', 'Lastname', 'Age'))
    #if request.method == 'POST':
        #formset = AuthorFormSet(request.POST, request.FILES)
        #if formset.is_valid():
            #formset.save()

    #else:
        #formset = AuthorFormSet()

    #context = {'segment': 'index', 'patient':patient.objects.all(), 'patient_form':formset}

    #html_template = loader.get_template('home/index.html')
    #return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    all_patients = patient.objects.all()
    return render(request,'home/index.html', {'all':all_patients})


@login_required(login_url="/login/")
def billing(request):
    if request.method == "POST":
        form = patientForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Your form has been submitted successfuly!'))
        return redirect('/')
    else:
        return render(request,'billing.html', {})


@login_required(login_url="/login/")
def updatebilling(request, pk):
    patient = patient.objects.get(id=pk)
    form = patientForm(instance=patient)
    context = {'form' :form}
    return render(request,'updatebilling.html', context)


    
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
