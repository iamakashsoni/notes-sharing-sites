from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=13, null=True)
    branch = models.CharField(max_length=30, null=True)
    role = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.signup.user.username+" "+self.status

