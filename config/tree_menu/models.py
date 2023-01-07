from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')
    title = models.CharField(max_length=100)
    number_page = models.IntegerField(default=1)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'