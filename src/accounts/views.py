from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

#Adjusted from register being a class to a function for proper
#django layout and format.
def register(request):
    #Instantiate empty form for user to view
    register_form = SignUpForm()

    #Establish lists and dicts used by both 'POST' and 'GET'
    #request methods (post = form submit, get = first time opening page)
    context = {}
    baseActFields = []
    otherFields0 = []
    otherFields1 = []
    otherFields2 = []
    otherFields3 = []
    infoString = 'Please give your current mailing address. If it changes during your time using this service, you can go into account settings to change it.'
    counter = 0
    baseActFieldNames = ['username', 'password1', 'password2']

    #If the user submitted their form
    if request.method=='POST':

        #Store the values of their form here from the SignUpForm function in accounts/forms.py
        form = SignUpForm(request.POST)

        #If no validation errors arise, we allow the user to submit the form
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')    #We will send the user to a verification notification
                                                #page, in the future, for now we send them to home page
        
        #If we have errors with the form validation, we send the user to the same page with all but their
        #password fields filled, however, we give them a popup of the errors with the form.
        
        else:
            #Holds the errors
            errors = []

            
            for field in form:

                #Put all the errors into the error list for display
                if(field.errors):
                    errors.append(field.errors)

                #We do this stuff here, like we do on a GET request, because
                #we want to keep their form data to avoid them having to re-enter it
                if(field.name in baseActFieldNames):
                    baseActFields.append(field)
                
                else:
                    
                    #Top row field elements of right half of form
                    if(counter < 3):
                        otherFields0.append(field)
                    
                    #Next row field element of right half of form
                    elif(counter < 4):
                        otherFields1.append(field)
                    
                    #3rd row field elements of right half of form
                    elif(counter < 6):
                        otherFields2.append(field)
                    
                    #4th row field elements of right half of form
                    else:
                        otherFields3.append(field)
                    
                    #This was a lazy solution to get the right half of
                    #the form to look pretty with how Django renders
                    #templates, should look into fixing this in the future?
                    counter += 1
            
            #Build the context, like with GET requests, but populate
            #the individual fields with the user data that we handled
            #in the previous for loop.
            context['errors'] = errors
            context['baseFields'] = baseActFields
            context['otherFields0'] = otherFields0
            context['otherFields1'] = otherFields1
            context['otherFields2'] = otherFields2
            context['otherFields3'] = otherFields3
            context['infoString'] = infoString

            #You must always return the render function, necessary for functionality
            #The inputs are "request" for the HTTP request, "template" for the template,
            #and "Context" for the context
            return render(request,'registration/register.html',context=context)
    
    #This assumes we received a "GET" request.
    else:
        #Build the fields that the user will see within the form.
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

        #Populate the areas of the context with values
        #necessary for the sign up form
        context['baseFields'] = baseActFields
        context['otherFields0'] = otherFields0
        context['otherFields1'] = otherFields1
        context['otherFields2'] = otherFields2
        context['otherFields3'] = otherFields3
        context['form'] = register_form
        context['infoString'] = infoString

        #See above for render function parameters
        return render(request,'registration/register.html',context=context)