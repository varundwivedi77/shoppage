
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='shopindex'),
    path('index/',views.index,name='shopindex'),
    path('about/',views.about,name='shopabout'),
    path('contact/',views.contact,name='shopcontact'),
    path('tracker/',views.tracker,name='shoptracker'),
    path('search/',views.search,name='shopsearch'),
    path('products/<int:myid>',views.productview,name='shopproductview'),
    path('checkout/',views.checkout,name='shopcheckout')




    
]