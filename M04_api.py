from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, ManyToManyField

# Model - Author, Fields - name, age
class Author(models.Model):
    name = CharField(max_length=100)
    age = IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Model - Genre, Fields - name
class Genre(models.Model):
    name = CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Model - Book, Fields - name, price, description, author(Author), genres(Genre)
class Book(models.Model):
    name = CharField(max_length=100)
    description = CharField(max_length=200)
    author = ForeignKey(Author, on_delete=CASCADE, related_name='books')
    genres = ManyToManyField(Genre, related_name='books')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'name: {self.name}, price: {self.price}'