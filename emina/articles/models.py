from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Articles(models.Model):
    categories = models.ManyToManyField(Categories)
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='articles/media/image', default=None)

    def __str__(self):
        return self.title

