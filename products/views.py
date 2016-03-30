## render es una funcion que nos permite renderizar contenido
from django.shortcuts import render

#del modulo http traemos HttpResponse
from django.http import HttpResponse

#importacion para cargar templates de html
from django.shortcuts import loader

#de ese modelo que necesito traer los productos para mandar los 
#datos a index.html
from .models import Product

'''
 views es nuestro controlador e interactuaremos entre la vista y el modelo.

 creamos una funcion llamada hola() y le mandamos el request y que retorne un httpresponse
'''
def hola(request):
	'''
	---------------------------------------------------------------------------------------
	#return HttpResponse('hola chicos') ---> no sera utilizado por ahora

	#ocupamos render para traer el html index.html
	##return render(request, 'index.html') ----> no es utilizado por ahora
	--------------------------------------------------------------------------------------- 
	'''
	'''
       creamos una variable llamada product y a esa variable le pasamos el objeto Product y 
       pedimos que los ordene por el id 
	'''
	product = Product.objects.order_by('id')


	'''
	creamos una variable llamada template y en esa variable a travez del metodo loader traemos la pagina index.html
	con la funcion get_template()
	'''
	template = loader.get_template('index.html')


	'''
	el contexto servira para poder ocupar todos los datos 
	respecto a el objeto product y llevarlos a index.html
	para ser ocupados alla con sintaxis django
	'''
	context = {
		'product': product
	}

	#le enviamos el contexto y el request a traves del httpResponse
	return HttpResponse(template.render(context, request))
