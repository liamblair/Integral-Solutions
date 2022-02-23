from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


def register(request):
    register_form = SignUpForm()
    context = {}
    baseActFields = []
    otherFields0 = []
    otherFields1 = []
    otherFields2 = []
    otherFields3 = []
    infoString = 'Please give your current mailing address. If it changes during your time using this service, you can go into account settings to change it.'
    counter = 0
    baseActFieldNames = ['username', 'password1', 'password2']
    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')    #We will send the user to a verification notification
                                                #page, in the future, for now we send them to home page
        else:
            errors = []

            for field in form:
                if(field.errors):
                    errors.append(field.errors)
                if(field.name in baseActFieldNames):
                    baseActFields.append(field)
                else:
                    if(counter < 3):
                        otherFields0.append(field)
                    elif(counter < 4):
                        otherFields1.append(field)
                    elif(counter < 6):
                        otherFields2.append(field)
                    else:
                        otherFields3.append(field)
                    counter += 1
            
            context['errors'] = errors
            context['baseFields'] = baseActFields
            context['otherFields0'] = otherFields0
            context['otherFields1'] = otherFields1
            context['otherFields2'] = otherFields2
            context['otherFields3'] = otherFields3
            context['infoString'] = infoString

            
            return render(request,'registration/register.html',context=context)
    else:
        for field in register_form:
            if(field.name in baseActFieldNames):
                baseActFields.append(field)
            else:
                if(counter < 3):
                    otherFields0.append(field)
                elif(counter < 4):
                    otherFields1.append(field)
                elif(counter < 6):
                    otherFields2.append(field)
                else:
                    otherFields3.append(field)
                counter += 1

        context['baseFields'] = baseActFields
        context['otherFields0'] = otherFields0
        context['otherFields1'] = otherFields1
        context['otherFields2'] = otherFields2
        context['otherFields3'] = otherFields3
        context['form'] = register_form
        context['infoString'] = infoString
        return render(request,'registration/register.html',context=context)