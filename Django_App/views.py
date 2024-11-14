from django.shortcuts import render

# Create your views here.

def test(request):

    return HttpResponse("Ok ,Done")
    #save customer
    c1 = customer( first_name="Saida", last_name="Ali" email="saida@x.com", dob="2000-11=08", gender="Male", weight=62)
    return HttpResponse(c1)


        #display data in our pages
        #loops
        #if statements
        #templating engine services