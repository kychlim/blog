from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    auth_author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField('작성자', max_length=20)
    title = models.CharField('제목', max_length=30, default="")
    contents = models.TextField('글내용', max_length=1000)
    # CharField는 한 둘, TextField는 여러 줄

    def __str__(self):
        return self.contents

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_text = models.TextField('댓글 내용', max_length=1000)
    comments_author = models.CharField('작성자', max_length=20, default="")

    def __str__(self):
        return  self.comments_text
