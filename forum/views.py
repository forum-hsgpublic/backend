# forum/views.py
from rest_framework import viewsets
from .models import Category, Post, Comment, Tag, PostTag
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, TagSerializer, PostTagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostTagViewSet(viewsets.ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer