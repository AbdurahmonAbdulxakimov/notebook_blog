from rest_framework import serializers

from .models import Author, ContactUsRequest, ContactUs, FAQ, Category, Tag, Post




# Contact Us Request Serializer
class ContactUsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'


# Contact Us Serializer
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


# FAQ Serializer
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
        
        
# Post Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
# Post Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )
    tag = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True,
        many=True
    )
    author = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True 
    )
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only=True

        
# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):    
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = '__all__'
        read_only = True