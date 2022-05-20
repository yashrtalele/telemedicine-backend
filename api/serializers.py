from dataclasses import fields
from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title',
            'content',
        ]
        model = Article