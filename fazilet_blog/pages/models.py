from django.db import models
from django.utils import timezone
class Page(models.Model):
	title = models.CharField(max_length=50)
	slug=models.CharField(max_length=50)
	content=models.TextField()
	is_active =models.BooleanField(default="False")
	icon =models.CharField(max_length = 10,default = " ")
	def __str__(self):
		return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    upload = models.ImageField(upload_to='uploads/',blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



