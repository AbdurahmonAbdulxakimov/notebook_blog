from rest_framework import routers 

from .views import PostPopularViewSet, PostFeaturedViewSet, PostViewSet, CategoryViewSet, TagViewSet
from .views import AuthorViewSet, AuthorTopViewSet, ContactUsRequestViewSet, ContactUsViewSet, FAQViewSet



router = routers.DefaultRouter()

# Author Routes
router.register(r'authors/top', AuthorTopViewSet, basename='author_top')
router.register(r'authors', AuthorViewSet, basename='author')

# Contact Routes
router.register(r'contact-us-requests', ContactUsRequestViewSet, basename='contact_us_request')
router.register(r'contact-us', ContactUsViewSet, basename='contact_us')

# General Routes
router.register(r'faqs', FAQViewSet, basename='faq')

# Post Routes
router.register(r'posts/popular', PostPopularViewSet, basename='post_popular')
router.register(r'posts/featured', PostFeaturedViewSet, basename='post_featured')
router.register(r'posts', PostViewSet, basename='post')

# Post Related
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')


urlpatterns = router.urls