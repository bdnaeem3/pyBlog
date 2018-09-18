from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - Posted By ' + self.author.username + ' - In ' + str(self.date_created.day) + '-' + str(self.date_created.month) + '-' + str(self.date_created.year)
