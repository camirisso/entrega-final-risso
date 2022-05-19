from django.urls import path
from EstudioApp import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Index"),
    path('about/', views.about,  name="About"),

    # CONSULTAS 
    # Leer consulta:
    path('form/list', views.consultas_list, name='consultas_list'),
    # Crear consulta:
    path('form/create', views.consulta_create, name='consulta_create'),
    # Actualizar consulta:
    path('form/update/<int:id>/', views.consulta_update, name='consulta_update'),
    # Borrar consulta:
    path('form/delete/<int:id>/', views.consulta_delete, name='consulta_delete'),
    # Url para búsqueda de consulta:
    path('search/', views.search, name='search'),

    # ABOGADO
    # CreateView
    path('abogado/form', views.AbogadoCrear.as_view(), name="abogado_form"),
    # Listview
    path('abogados/list', views.AbogadosLista.as_view(), name="abogado_list"),
    # DetailView
    path('abogados/<int:pk>/', views.AbogadoDetalle.as_view(), name="abogado_detail"),
    # UpdateView
    path('abogados/<int:pk>/update/', views.AbogadoActualizar.as_view(), name="abogado_update"),
    # DeleteView
    path('abogados/<int:pk>/delete/', views.AbogadoBorrar.as_view(), name="abogado_confirm_delete"),
    # Leer abogado
    #path('lawyer/list', views.abogados_list, name='abogados_list'),
    # Crear abogado:
    #path('lawyer/create', views.abogado_create, name='abogado_create'),
    # Actualizar abogado:
    #path('lawyer/update/<int:id>/', views.abogado_update, name='abogado_update'),
    # Borrar abogado:
    #path('lawyer/delete/<int:id>/', views.abogado_delete, name='abogado_delete'),

    # CLIENTE
    # Leer cliente:
    path('client/list', views.clientes_list, name='clientes_list'),
    # Crear cliente:
    path('client/create', views.cliente_create, name='cliente_create'),
    # Actualizar cliente:
    path('client/update/<int:id>/', views.cliente_update, name='cliente_update'),
    # Borrar cliente:
    path('client/delete/<int:id>/', views.cliente_delete, name='cliente_delete'),

    # SIGNUP
    path('signup/', views.signup_estudio, name = 'signup'),
    # LOGIN
    path('login/', views.login_estudio, name = 'login'),
    # LOGIN
    path('logout/', LogoutView.as_view(template_name='EstudioApp/index.html'), name = 'logout')
]
