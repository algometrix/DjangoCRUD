from django.db import models

# Create your models here.
class Foo(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table='foo'
    
class Bar(models.Model):
    fooid = models.ForeignKey(Foo,related_name='bar',db_column='fooid')
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table='bar'
