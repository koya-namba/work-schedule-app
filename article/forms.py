from django import forms

from .models import Article


class ManagerCreateArticleForm(forms.ModelForm):
    """管理者がarticleを作成するフォーム"""

    class Meta:
        model = Article
        fields = ('title', 'text',)

    def save(self, commit=False):
        article = super().save(commit=False)
        article.save()
        return article


class ManagerUpdateArticleForm(forms.ModelForm):
    """管理者がarticleを更新するフォーム"""

    class Meta:
        model = Article
        fields = ('title', 'text',)

    def save(self, commit=False):
        article = super().save(commit=False)
        article.save()
        return article


class StaffCreateArticleForm(forms.ModelForm):
    """スタッフがarticleを作成するフォーム"""

    class Meta:
        model = Article
        fields = ('title', 'text',)

    def save(self, commit=False):
        article = super().save(commit=False)
        article.save()
        return article


class StaffUpdateArticleForm(forms.ModelForm):
    """スタッフがarticleを更新するフォーム"""

    class Meta:
        model = Article
        fields = ('title', 'text',)

    def save(self, commit=False):
        article = super().save(commit=False)
        article.save()
        return article

