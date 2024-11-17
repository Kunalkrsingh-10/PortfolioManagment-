from django.shortcuts import render
from django.http import HttpResponse 
from .models import contact
from django.contrib import messages

# Create your views here.


#def home(request):
    #return render(request, "home.html") 

def contact(request):
    if request.method == "POST":
        print("post")
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        content=request.POST.get('content')
        print(name,email, content, number)
        if len(name)>1 and len(name)<30:
            pass
        else: 
            messages.error(request,"Length of name should be btw 1 and 30 characters")
            return render(request, 'home.html') 
        if len(email)>1 and len(email)<30:
            pass
        else: 
            messages.error(request,"Invalide email ,try again ")
        
        new_contact = contact(name=name, Email=email, Number=number, content=content)
        new_contact.save()
        messages.success(request, "Thank you for connecting me ") 
    return render(request, "home.html")    
