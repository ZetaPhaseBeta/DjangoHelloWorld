from django.db import models

class User(models.Model):
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    bio = models.CharField(max_length=1000)

    def  __str__(self):
        return self.name + '(' + self.username + ')' + ' - ' + self.bio

class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.title + ' created by ' + self.author
