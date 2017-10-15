from django.shortcuts import render,redirect
from .forms import householdform,personform,vehicleform
from .models import Household,Person,Vehicle
from django.http import HttpResponseRedirect

# Create your views here.

# def index(request):
#     form = householdform()
#     return render(request, 'personinfo/household.html', {'form': form})

tempHousehold = {
    'household': {'Address':'','Zipcode':'','City':'','State':'','Bedrooms':''},
    'person': {'Firstname':[],'Lastname':[],'Email':[],'Age':[],'Gender':[] },
    'vehicle':{'Make':[],'Modelname':[],'Year':[],'Licenceplate':[]},

}



def householdview(request):

    if request.method == "POST":
        # form = householdform(request.POST)
        # if form.is_valid():
        #     address = form.cleaned_data['address']
        #     zipcode = form.cleaned_data['zipcode']
        #     city = form.cleaned_data['city']
        #     state = form.cleaned_data['state']
        #     bedrooms = form.cleaned_data['bedrooms']
        #     # context = {'address':address,'zipcode':zipcode,'city':city,'state':state,'bedrooms':bedrooms}
        #     #h = Household.objects.Create(address,zipcode,city,state,bedrooms)
        # #     f = form.save()
        # Address = request.POST['Address']
        # Zipcode = request.POST['Zipcode']
        # City = request.POST['City']
        # State = request.POST['State']
        # Bedrooms = request.POST['Bedrooms']

        tempHousehold['household']['Address']= request.POST['Address']
        tempHousehold['household']['Zipcode']= request.POST['Zipcode']
        tempHousehold['household']['City']= request.POST['City']
        tempHousehold['household']['State']= request.POST['State']
        tempHousehold['household']['Bedrooms']= request.POST['Bedrooms']


        return redirect("/personview")

    else:
        # form = householdform()
        return render(request, 'personinfo/household.html')


def personview(request):
    if request.method == "POST":
        # #print("After post ")
        # form2 = personform(request.POST)
        # if form2.is_valid():
        #     #print("form is valid")
        #     data = form2.save()
        #     return redirect("/vehicleview")
        # Firstname = request.POST['Firstname']
        # Lastname = request.POST['Lastname']
        # Email = request.POST['Email']
        # Age = request.POST['Age']
        # Gender = request.POST['Gender']

        tempHousehold['person']['Firstname'].append(request.POST['Firstname'])
        tempHousehold['person']['Lastname'].append(request.POST['Lastname'])
        tempHousehold['person']['Email'].append(request.POST['Email'])
        tempHousehold['person']['Age'].append(request.POST['Age'])
        tempHousehold['person']['Gender'].append(request.POST['Gender'])

        print(tempHousehold['person'])

        return redirect("/vehicleview")

    else:
        # form2 = personform()
        return render(request, 'personinfo/person.html')

def vehicleview(request):
    if request.method == "POST":
        # #print("After post ")
        # form = vehicleform(request.POST)
        # if form.is_valid():
        #     #print("form is valid")
        #     data = form.save()
        #     return redirect("/listdata")
        tempHousehold['vehicle']['Make'].append(request.POST['Make'])
        tempHousehold['vehicle']['Modelname'].append(request.POST['Modelname'])
        tempHousehold['vehicle']['Year'].append(request.POST['Year'])
        tempHousehold['vehicle']['Licenceplate'].append(request.POST['Licenceplate'])
        print(tempHousehold['vehicle']['Make'])

        return redirect("/showforms")

    else:
        #form = vehicleform()
        return render(request, 'personinfo/vehicle.html')

def showforms(request):
    return render(request,'personinfo/list.html',{'tempHousehold':tempHousehold})


def savedata(request):
    form1 = Household(address=tempHousehold['household']['Address'],zipcode=tempHousehold['household']['Zipcode'],city=tempHousehold['household']['City'],state=tempHousehold['household']['State'],bedrooms=tempHousehold['household']['Bedrooms'])
    form1.save()
    for i in range(len(tempHousehold['person']['Firstname'])):
        form2 = Person(household=form1,first_name=tempHousehold['person']['Firstname'][i],last_name=tempHousehold['person']['Lastname'][i],email=tempHousehold['person']['Email'][i],age=tempHousehold['person']['Age'][i],gender=tempHousehold['person']['Gender'][i])
        form2.save()
    for i in range(len(tempHousehold['vehicle']['Make'])):
        form3 = Vehicle(person=form2,household=form1,make=tempHousehold['vehicle']['Make'][i],model_name=tempHousehold['vehicle']['Modelname'][i],year=tempHousehold['vehicle']['Year'][i],liceance_plate=tempHousehold['vehicle']['Licenceplate'][i])
        form3.save()

    return render(request,'personinfo/list.html')
