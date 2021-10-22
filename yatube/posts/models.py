from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, SlugField, TextField
from django.db.models.fields.related import ForeignKey

User = get_user_model()

class Group(models.Model):
    title = CharField(max_length=200)
    slug = SlugField()
    description = TextField()

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    group = ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='posts')