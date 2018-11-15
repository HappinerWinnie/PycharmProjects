from django.db import models
# Create your models here.


class Users(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True, primary_key=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    # 元数据里定义用户按创建时间的反序排列，也就是最近的最先显示；
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=30)
    id  = models.CharField(max_length=30,primary_key=True)


class Production(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    addr = models.CharField(max_length=30)

class Ingre(models.Model):
    name = models.CharField(max_length=30,primary_key=True)

class Foods(models.Model):
    name = models.CharField(max_length=30)
    id = models.CharField(max_length=30,primary_key=True)
    price = models.IntegerField()
    sum = models.IntegerField()

    cls = models.ForeignKey('Class')
    production = models.ForeignKey('Production')

    ingre = models.ManyToManyField('Ingre')