from django.db import models


class Category(models.Model):
    title=models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.title
    

class Video(models.Model):
    title=models.CharField( max_length=100)
    image=models.ImageField( upload_to='static/images' )
    video=models.FileField( upload_to='static/videos')
    channal_name=models.CharField( max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    add_date=models.DateField(  auto_now=True)
    discription=models.CharField( max_length=200)

    def __str__(self) -> str:
        return self.title