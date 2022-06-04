from django.urls import path
from EstudioApp import views 

urlpatterns = [
    path('', views.inicio, name="Index"),
    path('about/', views.about,  name="About"),

    # AVATAR
    path('agregar-avatar', views.agregarAvatar, name = "agregar-avatar"),

    # POST urls
    path('posts/', views.PostView.as_view(),  name="posts"),
    path('articulo/<int:pk>', views.ArticleDetailView.as_view(),  name="article-detail"),
    path('add_post/', views.AddPostView.as_view(),  name="add-post"), 
    path('articulo/update/<int:pk>', views.UpdatePostView.as_view(),  name="update-post"), 
    path('articulo/<int:pk>/delete', views.DeletePostView.as_view(),  name="delete-post"), 

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

    # CLIENTE
    # Leer cliente:
    path('client/list', views.clientes_list, name='clientes_list'),
    # Crear cliente:
    path('client/create', views.cliente_create, name='cliente_create'),
    # Actualizar cliente:
    path('client/update/<int:id>/', views.cliente_update, name='cliente_update'),
    # Borrar cliente:
    path('client/delete/<int:id>/', views.cliente_delete, name='cliente_delete'),
]
