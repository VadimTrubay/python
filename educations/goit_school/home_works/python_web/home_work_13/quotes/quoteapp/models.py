from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    born_date = models.CharField(max_length=50, null=False, unique=True)
    born_location = models.CharField(max_length=500, null=False, unique=False)
    description = models.CharField(max_length=5500, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.tag}"

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})


class Quote(models.Model):
    quote = models.CharField(max_length=5000, null=False)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})