from django.db import models
from django.contrib import admin



#class Photo(models.Model):
#    item = models.ForeignKey(Item)
#    title = models.CharField(max_length=100)
#    #image = models.ImageField(upload_to='photos')
#    image = ThumbnailImageField(upload_to='photos')
#    caption = models.CharField(max_length=250, blank=True)
#    
#    class Meta:
#        ordering = ["title"]
#        
#    def __unicode__(self):
#        return self.title
#    
#    @models.permalink
#    def get_absolute_url(self):
#        return ('photo_detail', None, {'object_id':self.id})
    

class Photo(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    datetime = models.TextField()
    imageName = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    
    class Meta:
        ordering = ["-datetime"]
    
    def __unicode__(self):
        return self.title

        
        
        
