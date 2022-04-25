from django.urls import path
from EstudioApp import views 

urlpatterns = [
    path('', views.inicio, name="Index"),
    path('about/', views.about,  name="About"),
    path('post/', views.post,  name="Post"),
    # Vista al formulario de consulta:
    path('form/', views.form, name='form'),
# Vista al formulario de cliente:
    path('client/', views.form_cliente, name='client'),
    # Vista al formulario de abogado:
    path('lawyer/', views.form_abogado, name='lawyer'),
    # Vista para búsqueda de consulta:
    path('search/', views.search, name='search'),
]
