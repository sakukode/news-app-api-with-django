# import class yang dibutuhkan untuk membuat view
from django.http import Http404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# import class untuk otentikasi rest api
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# import package untuk menambahkan judul & deskripsi pada dokumentasi API
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

# import class models dari aplikasi newsapp
from .models import Category, News, Comment
# import class serializers dari aplikasi newsapp
from .serializers import CategoryListSerializer, CategoryDetailSerializer, NewsListSerializer, NewsDetailSerializer, CommentFormSerializer
# import class Filter untuk custom fitur filtering
from .filters import NewsFilter

# Membuat View untuk API endpoint "Get All Categories"
# /api/category
@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Get List of Categories',
                                                            operation_description='Returns a paginated array of Categories.'))
class CategoryListView(ListAPIView):
    # mengeset class serializers
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    # Menambahkan fitur filtering, searching dan ordering
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    # mengeset fields/kolom untuk fitur filtering
    filter_fields = ['name']
    # mengeset fields/kolom untuk fitur searching
    search_fields = ['name']
    # mengeset fields/kolom untuk fitur ordering
    ordering_fields = ['name', 'created_at']
    # mengeset fields/kolom default untuk fitur ordering
    ordering = ['created_at']
    # menambahkan otentikasi
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]


# Membuat View untuk API endpoint "Get Detail of Category"
# /api/category/:id
@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Get Detail of Category',
                                                            operation_description='Return a single Category by id.'))
class CategoryDetailView(RetrieveAPIView):
    # mengeset class serializers
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    # menambahkan otentikasi
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
 

# Membuat View untuk API endpoint "Get List of News"
# /api/news
@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Get List of News',
                                                            operation_description='Returns a paginated array of published News.'))
class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    # mengambil data news/berita yang hanya berstatus published
    queryset = News.objects.is_published()

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    # mengeset fields/kolom untuk fitur filtering dengan class NewsFilter (custom filter)
    filterset_class = NewsFilter
    # mengeset fields/kolom untuk fitur searching
    search_fields = ['title']
    # mengeset fields/kolom untuk fitur ordering
    ordering_fields = ['title', 'created_at']
    # mengeset fields/kolom default untuk fitur ordering
    ordering = ['created_at']
    # menambahkan otentikasi
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]


# Membuat View untuk API endpoint "Get Detail of News"
# /api/news/:id
@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Get Detail of News',
                                                            operation_description='Return a single News by id.'))
class NewsDetailView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    # mengambil data news/berita yang hanya berstatus published
    queryset = News.objects.is_published()
    # menambahkan otentikasi
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]


# Membuat View untuk API endpoint "Create New Comment on News"
# /api/news/:id/comment
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='Create New Comment on News',
                                                             operation_description='Create a new comment on news.'))
class NewsCreateCommentView(CreateAPIView):
    serializer_class = CommentFormSerializer
    queryset = Comment.objects.all()
    # menambahkan otentikasi
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
	# meng-override method perform_create untuk mengambil news_id dari parameter url API endpoint
	# Kemudian disimpan pada kolom news_id di tabel Comment pada saat kita melakukan requets endpoint ini.
    def perform_create(self, serializer):
        news_id = self.kwargs['pk']
        try:
            news = News.objects.get(pk=news_id)
            serializer.save(news_id=news.id)
        except News.DoesNotExist:
            raise Http404
