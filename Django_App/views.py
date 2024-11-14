from django.forms.boundfield.BoundField import template_name
from django.shortcuts import render

from Django_App.models import Customer


# Create your views here.

# def test(request):
#
#     return HttpResponse("Ok ,Done")
#     #save customer
#     c1 = customer( first_name="Saida", last_name="Ali" email="saida@x.com", dob="2000-11=08", gender="Male", weight=62)
#     return HttpResponse(c1)
#
#
#         #display data in our pages
#         #loops
#         #if statements
#         #templating engine services

def customers(request):
    data = Customer.objects.all() # select * from customers
    return render( request, template_name:"customers.html", context:{"customer":data})