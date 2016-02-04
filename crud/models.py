from django.db import models
import uuid

# Create your models here.
class Foo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,db_column='foo_id')
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table='foo'
    
class Bar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,db_column='bar_id')
    foo = models.ForeignKey(Foo,related_name='bar',db_column='foo_id')
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table='bar'
