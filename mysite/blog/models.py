from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add= True)
    slug = models.SlugField()
    description = models.TextField()
    content = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('blog',[self.slug])

    def __unicode__(self):
        return self.title

    class Meta :
        ordering = ['-added']
