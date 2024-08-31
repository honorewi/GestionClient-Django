from django.db import models
from client.models import Client
from produit.models import Produits

# Create your models here.
class Commande(models.Model):
    STATUS=(('en instance','en instance'),
           ('non livré','non livé'),
           ('livré','livré'),
    )
    client=models.ForeignKey(Client,null=True,on_delete= models.SET_NULL)
    produit=models.ForeignKey(Produits,null=True,on_delete= models.SET_NULL)
    statuts=models.CharField(max_length=200, null=True,choices=STATUS)
    date_creation= models.DateTimeField(auto_now_add=True)
