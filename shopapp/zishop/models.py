from django.db import models
'''
1.模型需要继承models.Model
2.系统会自动添加一个主键--id
3.字段
    字段名=model.类型（选项）
    字段名是数据表的字段名
    字段名不要使用python，mysql的关键字
'''
# Create your models here.
class Book(models.Model):
    bname = models.CharField(max_length=10)
    bpages = models.IntegerField(max_length=100)
    def str():
        return self

class hero(models.Model):
    hname = models.CharField(max_length=10)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)