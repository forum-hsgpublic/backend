# forum/serializers.py
from rest_framework import serializers
from .models import Category, Post, Comment, Tag, PostTag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'content', 'created_date', 'last_updated_date', 'user', 'category']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'content', 'created_date', 'post', 'user']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_id', 'name']

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ['post', 'tag']