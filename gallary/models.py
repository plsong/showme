from django.db import models

# Create your models here.


class Gallary(models.Model):
    description=models.CharField(default='在这里写作品的简介',max_length=100)
    image = models.ImageField(default='defualt.png',upload_to='images/')
    title = models.CharField(default='作品标题',max_length=50)

    def __str__(self):
        return self.title # 这个函数创建