from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    allContent = models.CharField(max_length=1000)
    publication_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title


class Center(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    imgurl = models.CharField(max_length=100, null=True)
    urlButton = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=30)
    allContent = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title


class RContent(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    allContent = models.CharField(max_length=1000)
    publication_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=30)
    member = models.CharField(max_length=30)
    status = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return self.name


class JoinMe(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    myclass = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    describe = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50, null=True)


class Activities(models.Model):
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=300, null=True)
    author = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30)
    create_time = models.DateField(max_length=50)

    def __unicode__(self):
        return self.title


class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    num = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    describe = models.CharField(max_length=300)
    myactivities = models.ForeignKey(JoinMe)

    def __unicode__(self):
        return self.fullname


class Meta:
        ordering = ['-project']