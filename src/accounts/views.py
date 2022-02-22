from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

def register(request):
    register_form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #User model fields will go here, underlying principle of this
            #page now works.

            form.save()

            return HttpResponseRedirect('/')    #We will send the user to a verification notification
                                                #page, in the future, for now we send them to home page
        else:
            print("Invalid Form")
            context = {}
            context['form'] = form
            return render(request,'registration/register.html',context)
    else:
        return render(request,'registration/register.html',{'form':register_form})