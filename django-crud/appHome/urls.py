from django.urls import path
from . import views

urlpatterns = [
    path('', views.fazerLogin, name="fazerLogin"),
    path('adicionar-login', views.add_login, name="add_login"),
    path('home/', views.appHome, name="appHome"),
    path('excluir/<int:id_produto>', views.excluir_Produto, name = "excluir_Produto"),
    path('adicionar', views.add_Produto, name="add_Produto"),
    path('editar/<int:id_produto>', views.editar_Produto, name="editar_Produto"),
    path('vendas', views.mostrarProdutos, name="vendas"),
]   