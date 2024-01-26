from rest_framework import viewsets, mixins, filters

from .models import FAQ, Author, ContactUs, ContactUsRequest, Category, Tag, Post
from .serializers import AuthorSerializer, ContactUsRequestSerializer, ContactUsSerializer, FAQSerializer, CategorySerializer, TagSerializer, PostSerializer



# # # # #  AUTHOR # # # # #

# Author List & Retrieve
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
# Author Top List & Retrieve
class AuthorTopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.filter(is_top=True)
    serializer_class = AuthorSerializer


# # # # #  CONTACT # # # # #

# Contact Us Request Create
class ContactUsRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactUsRequest.objects.all()
    serializer_class = ContactUsRequestSerializer


# ContactUs List & Retrieve
class ContactUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


# # # # #  FAQ # # # # #

# FAQ List & Retrieve
class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# # # # #  CATEGORY & TAG # # # # #

# Category List & Retrieve
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PostSerializer


# Tag List & Retrieve
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = PostSerializer


# # # # #  POST # # # # #

# Posts List & Retrieve
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tag__title', 'category__title']


# Posts Featured List & Retrieve
class PostFeaturedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_featured=True)
    serializer_class = PostSerializer


# Posts Popular List & Retrieve
class PostPopularViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_popular=True)
    serializer_class = PostSerializer
    

# Posts Related to Author
class PostsRelatedTOAuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer