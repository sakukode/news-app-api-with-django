# import class serializers
from rest_framework.serializers import ModelSerializer

# import user model
from django.contrib.auth.models import User
# import class model lain
from .models import Category, News, Comment


# Membuat class Serializers untuk API endpoint "Get List of Categories"
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', )


# Membuat class Serializers untuk API endpoint "Get Detail of Category"
class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', )


# Membuat class UserSerializer yang akan berelasi ke NewsSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


# Membuat class CommentListSerializer yang akan berelasi ke NewsSerializer
class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at', )


# Membuat class CommentFormSerializer yang akan berelasi ke NewsSerializer
class CommentFormSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)


# Membuat class NewsListSerializer untuk API endpoint "Get List of News"
class NewsListSerializer(ModelSerializer):
    user = UserSerializer(read_only=True) # relasi ke modul/tabel user
    categories = CategoryListSerializer(many=True, read_only=True) # relasi ke modul/tabel category

    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'user', 'categories', 'published_at')

 
# Membuat class NewsDetailSerializer untuk API endpoint "Get Detail of News"
class NewsDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True) # relasi ke modul/tabel user
    categories = CategoryListSerializer(many=True, read_only=True) # relasi ke modul/tabel category
    comments = CommentListSerializer(many=True, read_only=True, source='comment_set') # relasi ke modul/tabel comment

    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'content', 'cover', 'published_at', 'user', 'categories', 'comments', )
