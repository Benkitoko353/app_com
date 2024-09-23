from django.shortcuts import render
from app_commande.models import Categorie,Produit
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CategorieSerialiser
from .models import*
from django.core.paginator import Paginator



# Create your views here.




def home (request):
    nbrcategorie = Categorie.objects.all().count() 
    nbrproduit = Produit.objects.all().count()

    ctx = {
         'nbrcategorie':nbrcategorie,
         'nbrproduit':nbrproduit,
    } 

    return render(request, 'home.html',ctx)

def categorie (request):

    cats = Categorie.objects.all()

    p = Paginator(cats, 1)
    page = request.GET.get('page')
    categoris =p.get_page(page)

    cxt = {
        'cats': categoris
    }
        

    return render(request, 'categorie.html',cxt)

def ajouterCategorie(request):

    return render(request, 'ajouterCategorie.html')


def addCategorie(request):
    message = None
    if request.method == 'POST':
        codecat = request.POST["code"]
        libcat = request.POST["libelle"]

        rs_cats= Categorie.objects.filter(code=codecat)

    if len(rs_cats)>0:
            message = "Ce code categorie existe"
    else:
            
            cates = Categorie(            
                code = codecat,
                libelle = libcat,
            )

            cates.save()
            message = "categorie enregistré avec succès"

    ctx ={
        'message':message
    }
    return render(request,'ajouterCategorie.html',ctx)

def deleteCategorie(request, id):

    cat = Categorie.objects.get(pk=id)
    cat.delete()

    return redirect('/categorie/')

def modifierCategorie(request,id):
     
  c = Categorie.objects.get(pk=id)

  ctx = {
          'c':c
     }
  return render(request,'modifierCategorie.html',ctx)

def updateCategorie(request,id):
     c = Categorie.objects.get(pk=id)
     lib = request.POST["libelle"]

     c.libelle = lib
     c.save()
     return redirect('/categorie/')

#PRODUIT

def produit(request):

    pr = Produit.objects.all()

    p = Paginator(pr, 1)
    page = request.GET.get('page')
    prodis =p.get_page(page)


    cxt = {
        'pr': prodis
    }


    return render(request, 'produit.html',cxt)

def ajouterProduit(request):

    cats = Categorie.objects.all()

    ctx = {
         'cats': cats
    }

    return render(request, 'ajouterProduit.html',ctx)

def deleteProduit(request, id):

    prod = Produit.objects.get(pk=id)
    prod.delete()

    return redirect('/produit/')

def modifierProduit(request,id):
     
  p = Produit.objects.get(pk=id)

  produ = {
          'p':p
     }
  return render(request,'modifierProduit.html',produ)

def updateProduit(request,id):
     c = Produit.objects.get(pk=id)
     lib = request.POST["libelle"]

     c.libelle = lib
     c.save()
     return redirect('/produit/')

def addProduit(request):
    message = None
    if request.method == 'POST':
        code = request.POST["code"]
        libprod = request.POST["libelle"]
        qte = request.POST["qte"]
        pu = request.POST["pu"]
        categorie = request.POST["categorie"]
        

        rs_pr= Produit.objects.filter(code=code)
        cat= Categorie.objects.get(code=categorie)

    if len(rs_pr)>0:
            message = "Ce produit existe"
    else:
        prod = Produit(
             code = code,
             libelle = libprod,
             qte = qte,
             pu = pu,
             Categorie = cat,
        )
        
        prod.save()
        message = "produit enregistré avec succès"
    ctx ={
        'message':message
    }
    return render(request,'ajouterProduit.html',ctx)

# Création des Apis pour le modèle Categorie

class CategorieDetails(APIView):
    def get(self,request):
          
        obj = Categorie.objects.all()
        serializer = CategorieSerialiser(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
     

    def post(self,request):
          
        serializer = CategorieSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)






