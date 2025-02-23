from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Post(TranslatableModel):
  translations = TranslatedFields(
        title = models.CharField(max_length=150, verbose_name=_("titulo"), null=True),
        content = models.TextField(verbose_name=_("contenido"))
    ) 
  
  image = models.ImageField(upload_to='blog/images/')
  youtube = models.URLField(blank=True)
  date = models.DateField(datetime.date.today)

  # def __str__(self):
  #     return self.title
  def __unicode__(self):
        return self.title
        
  class Meta:
        ordering = ['-id']  # Ordena por ID descendente        
  
