"""
URL configuration for gstcom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_commande.views import home,categorie,ajouterCategorie,addCategorie,deleteCategorie,modifierCategorie,updateCategorie,produit,deleteProduit,modifierProduit,updateProduit,ajouterProduit,addProduit,CategorieDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('categorie/', categorie, name="categorie"),
    path('ajouterCategorie/', ajouterCategorie, name="ajouterCategorie"),
    path('addCategorie/', addCategorie, name="addCategorie"),
    path('deleteCategorie<str:id>/', deleteCategorie, name="deleteCategorie"),
    path('modifierCategorie<str:id>/', modifierCategorie, name="modifierCategorie"),
    path('updateCategorie<str:id>/', updateCategorie, name="updateCategorie"),
    path('apicategorie/',CategorieDetails.as_view(), name="apicategorie"),
    # Produit
    path('produit/', produit, name="produit"),
    path('deleteProduit<str:id>/', deleteProduit, name="deleteProduit"),
    path('modifierProduit<str:id>/', modifierProduit, name="modifierProduit"),
    path('updateProduit<str:id>/', updateProduit, name="updateProduit"),
    path('ajouterProduit/', ajouterProduit, name="ajouterProduit"),
    path('addProduit/', addProduit, name="addProduit"),


    
    
    

    

]
