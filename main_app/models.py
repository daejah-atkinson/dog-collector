from django.db import models

class Dog(models.Model):

    breed = models.CharField(max_length=100)
    img = models.CharField(max_length=550)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.breed

    class Meta:
        ordering = ['breed']


class Group(models.Model):

    type = models.CharField(max_length=150)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        return self.type

class Rescue(models.Model):
    name = models.CharField(max_length=150)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='rescues')

    def __str__(self):
        return self.name