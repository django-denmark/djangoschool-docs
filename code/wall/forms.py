from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'text',)

    def clean_text(self):
        text = self.cleaned_data['text']

        if 'cake' not in text.lower():
            raise forms.ValidationError("I only want comments about cake!!")

        return text
