from rest_framework import serializers
from .models import*

class CategorieSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"