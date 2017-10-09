from django.shortcuts import render,redirect
from .forms import householdform,personform,vehicleform
from .models import Household,Person,Vehicle
from django.http import HttpResponseRedirect

# Create your views here.

# def index(request):
#     form = householdform()
#     return render(request, 'personinfo/household.html', {'form': form})

def householdview(request):

    if request.method == "POST":
        form = householdform(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            bedrooms = form.cleaned_data['bedrooms']
            # context = {'address':address,'zipcode':zipcode,'city':city,'state':state,'bedrooms':bedrooms}
            #h = Household.objects.Create(address,zipcode,city,state,bedrooms)
            f = form.save()

            return redirect("/personview")

    else:
        form = householdform()
    return render(request, 'personinfo/household.html', {'form':form})


def personview(request):
    if request.method == "POST":
        #print("After post ")
        form2 = personform(request.POST)
        if form2.is_valid():
            #print("form is valid")
            data = form2.save()
            return redirect("/vehicleview")

    else:
        form2 = personform()
    return render(request, 'personinfo/person.html', {'form2': form2})

def vehicleview(request):
    if request.method == "POST":
        #print("After post ")
        form = vehicleform(request.POST)
        if form.is_valid():
            #print("form is valid")
            data = form.save()
            return redirect("/listdata")

    else:
        form = vehicleform()
    return render(request, 'personinfo/vehicle.html', {'form': form})

def listdataview(request,id):
    h = Household.objects.get(pk=id)
    #p = Person.objects.get(pk=id)
    #v = Vehicle.objects.get(pk=id)
    context = {
    'H':h,
    }
    return render(request,'personinfo/list.html',context)
