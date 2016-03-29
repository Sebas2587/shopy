
#incluimos include en la importacion de urls
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
#esta url nos lleva admin
    url(r'^admin/', admin.site.urls),
    #ocupamos include para traer las url de la aplicacion product hacia la aplicacion global
    #esta url 
    url(r'^', include('products.urls')),# a ese diagonal incluye products.urls
]
