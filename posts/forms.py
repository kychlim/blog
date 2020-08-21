from django import forms
from posts.models import Post
from posts.models import Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']     # 자동으로 input할 컬럼명

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_author', 'comments_text']