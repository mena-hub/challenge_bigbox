from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()
    order = models.IntegerField(default=0, verbose_name=u'orden')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Reason(CommonInfo):  
    pass 
    
class Category(CommonInfo):    
    description = models.TextField(verbose_name=u'descripción')

class Product(models.Model):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='categoría')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Activity(Product):
    reasons = models.ManyToManyField(Reason, blank=True, verbose_name='tags')
    purchase_available = models.BooleanField(default=False, verbose_name='disponible venta individual')

class Box(Product):
    activities = models.ManyToManyField(Activity, verbose_name="actividades") # !!! Lo importante
    price = models.IntegerField(verbose_name='precio de venta')
    purchase_available = models.BooleanField(default=False, verbose_name='disponible venta individual')
    slug = models.CharField(max_length=20, null=True, blank=True) # blank=True <-- No, a futuro