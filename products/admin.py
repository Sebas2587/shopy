from django.contrib import admin

#importamos el modelo de product llamado Product
from .models import Product


# utilizamos decorador que es una funcion 
#externa a este codigo y registramos producto al 
#administrador pero esto lo hace con la clase adminproduct
@admin.register(Product)

class AdminProduct(admin.ModelAdmin):

	#desplegar los nombres que queremos ver con list_display
	list_display = ('name', 'category', 'description', 'price',)
	#fitraremos por categoria con list_filter
	list_filter = ('category',)