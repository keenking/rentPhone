from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # 999999.99
    pub_date = models.DateTimeField()
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # ad=models.ForeignKey(to="AuthorDetail",to_field="id",on_delete=models.CASCADE,unique=True)
    ad = models.OneToOneField(to="AuthorDetail", to_field="id", on_delete=models.CASCADE, )

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    gf = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    last_time = models.DateTimeField()