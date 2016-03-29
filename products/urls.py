#para esta aplicacion se crean las url correspondientes (solo para esta aplicacion) 
from django.conf.urls import url
#importamos la views que esta en esta aplicacion 
from .import views

#creamos el diccionario
#creamos una url interna en la aplicaicon y hay que crearla a nivel de proyecto
urlpatterns = [
	url(r'^$', views.hola, name ='hello')# $ --> raizdel sitio

]