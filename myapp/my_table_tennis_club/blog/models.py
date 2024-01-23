from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'My Blog'
    verbose_name_plurals = 'My Blogs'
