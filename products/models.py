from __future__ import unicode_literals

from django.db import models

class Product(models.Model):

	#atributos para nuestro modelo de tablas producto
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	
	#para manejar concurrencias economicas utilizar DecimalField
	price = models.DecimalField(max_digits=6, decimal_places=2)

#creamos una funcion reservada para devolver el nombre del objeto.
#de lo que creaste de ese mismo objeto traer el nombre
	def __str__(self):
		return self.name

    