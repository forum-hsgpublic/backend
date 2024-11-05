# forum/serializers.py
from rest_framework import serializers
from .models import User, Category, Post, Comment, Tag, PostTag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'login_id',
            'email',
            'join_date',
            'last_login',
            'is_superuser',
            'is_active',
            'is_staff'
        ]

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['login_id', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            login_id=validated_data['login_id'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

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