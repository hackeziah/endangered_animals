from django.db import models

# Create your models here.

class Post(models.Model):

    PUBLISH = 0
    NOT_PUBLISH = 1

    STATUS = (
        (PUBLISH, "Publish"),
        (NOT_PUBLISH, "Not Publish"),
    )

    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    status = models.IntegerField(verbose_name="Status", choices=STATUS,default = 0)
    created_by = models.CharField(verbose_name="Created By", max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commented_by = models.CharField(verbose_name="Created By", max_length=200)
    comment = models.TextField(max_length=2000, help_text="Comments..")
    post = models.CharField(verbose_name="Post Ref", max_length=200)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.post
