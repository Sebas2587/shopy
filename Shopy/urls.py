
#incluimos include en la importacion de urls
from django.conf.urls import url, include

from django.contrib import admin
#traemos settings  y static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

#esta url nos lleva admin
    url(r'^admin/', admin.site.urls),

    #ocupamos include para traer las url de la aplicacion product hacia la aplicacion global
    #esta url 
    url(r'^', include('products.urls')),# a ese diagonal incluye products.urls
#hacemos una adicion de static pasarle los valores a  media root y media url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
