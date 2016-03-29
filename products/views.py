## render es una funcion que nos permite renderizar contenido
from django.shortcuts import render
#del modulo http traemos HttpResponse
from django.http import HttpResponse
#funcion que sirve para cargar templates de html
from django.shortcuts import loader
#de ese modelo que necesito traer los productos
from .models import Product


# views es nuestro controlador e interactuaremos 
#entre la vista y el modelo.


#creamos una funcion y le mandamos el request y que retornte un httpresponse

def hola(request):
	#return HttpResponse('hola chicos') no sera utilizado por ahora
	#ocupamos render para traer el html index.html
	##return render(request, 'index.html')


	#
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'product': product


	}
	#le enviamos el contexto y el request
	return HttpResponse(template.render(context, request))
