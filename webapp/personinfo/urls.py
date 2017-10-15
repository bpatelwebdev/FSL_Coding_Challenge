from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^',views.index,name = 'index'),
    url(r'^$',views.householdview,name='household'),
    url(r'^personview/$',views.personview,name='personview'),
    url(r'^vehicleview/$',views.vehicleview,name='vehicleview'),
    url(r'^showforms/$',views.showforms,name='showforms'),
    url(r'^savedata/$',views.savedata,name='savedata'),

]
