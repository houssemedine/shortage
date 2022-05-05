from django.db import models

# Create your models here.


class MB52(models.Model): #Model MB52
    # uploaded_by = models.IntegerField()
    # uploaded_at= models.TimeField()
    material = models.CharField(max_length=30,null=True) #Numéro d'article	
    division = models.CharField(max_length=20,null=True) #Division
    store = models.CharField(max_length=10,null=True) #Magasin
    store_level_deletion_indicator =models.CharField(max_length=15,null=True) #Tém.suppr.:niv. mag	
    unit=models.CharField(max_length=5,null=True) #Unité de qté base
    for_free_use= models.FloatField(null=True) #A utilisation libre	
    currency=models.CharField(max_length=5,null=True) #Devise	
    value_free_use=models.FloatField(null=True)#Val. utilis. libre
    transit_transfer=models.FloatField(null=True) #Transit et transfert
    transit_transfer_value = models.FloatField(null=True) #Val. en Trnst&Tsft	
    in_quality_control = models.FloatField(null=True) #En contrôle qualité	
    value_quality_control = models.FloatField(null=True) #Val. ds ctrl.qual.	
    non_free_stock=models.FloatField(null=True) #Stock non libre	
    non_free_value =models.FloatField(null=True) #Valeur non libre
    blocked=models.FloatField(null=True) #Bloqué	
    blocked_stock_value=models.FloatField(null=True) #Val. stock bloqué	
    returns=models.FloatField(null=True) #Retours	
    blocked_return_stock_value=models.FloatField(null=True) #Val.stk ret.bloq.


    # def uploded_at_time(self):
    #     return self.uploaded_at.datetime.now()
    # def uploaded_by_user(self):
    #     return self

    