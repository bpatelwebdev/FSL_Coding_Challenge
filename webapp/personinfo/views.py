from django.shortcuts import render, redirect

from .models import Household, Person, Vehicle

# Create your views here.

# def index(request):
#     form = householdform()
#     return render(request, 'personinfo/household.html', {'form': form})

tempHousehold = {
    'household': {'Address': '', 'Zipcode': '', 'City': '', 'State': '', 'Bedrooms': ''},
    'persons': [{'Firstname': '', 'Lastname':'', 'Email': '', 'Age': '', 'Gender': ''}],
    'vehicles': [{'Make': '', 'Modelname': '', 'Year': '', 'Licenceplate': ''}],
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

        tempHousehold['household']['Address'] = request.POST['Address']
        tempHousehold['household']['Zipcode'] = request.POST['Zipcode']
        tempHousehold['household']['City'] = request.POST['City']
        tempHousehold['household']['State'] = request.POST['State']
        tempHousehold['household']['Bedrooms'] = request.POST['Bedrooms']

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
        person = {
            'Firstname': request.POST['Firstname'],
            'Lastname': request.POST['Lastname'],
            'Email': request.POST['Email'],
            'Age': request.POST['Age'],
            'Gender': request.POST['Gender']
        }
        tempHousehold['persons'].append(person)
        print(tempHousehold['persons'])

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
        vehicle = {
            'Make':request.POST['Make'],
            'Modelname':request.POST['Modelname'],
            'Year':request.POST['Year'],
            'Licenceplate':request.POST['Licenceplate']

        }
        tempHousehold['vehicles'].append(vehicle)
        print(tempHousehold['vehicles'])

        return redirect("/showforms")

    else:
        # form = vehicleform()
        return render(request, 'personinfo/vehicle.html')


def showforms(request):
    return render(request, 'personinfo/list.html', {'tempHousehold': tempHousehold})


def savedata(request):
    dbHousehold = Household(address=tempHousehold['household']['Address'],
                            zipcode=tempHousehold['household']['Zipcode'],
                            city=tempHousehold['household']['City'], state=tempHousehold['household']['State'],
                            bedrooms=tempHousehold['household']['Bedrooms'])
    dbHousehold.save()

    for person in tempHousehold['persons']:
        dbperson = Person(household=dbHousehold, first_name=person['Firstname'],
                          last_name=person['Lastname'], email=person['Email'],
                          age=person['Age'], gender=person['Gender'])
        dbperson.save()
    for vehicle in tempHousehold['vehicles']:
        dbvehicle = Vehicle(person=dbperson, household=dbHousehold, make=vehicle['Make'],
                        model_name=vehicle['Modelname'], year=vehicle['Year'],
                        liceance_plate=vehicle['Licenceplate'])
        dbvehicle.save()

    return render(request, 'personinfo/list.html')
