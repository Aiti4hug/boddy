from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['product_image']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'stars']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer
    date = serializers.DateField(format('%m-%d-%Y'))

    class Meta:
        model = Review
        fields = ['user', 'text', 'date']


class ProductListSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'photos', 'product_name', 'price', 'owner',
                  'get_avg_rating', 'get_count_people']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class ProductLDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    category = CategorySimpleSerializer()
    created_date = serializers.DateField(format('%m-%d-%Y'))
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'check_origin',
                  'product_video', 'photos', 'price', 'owner', 'created_date',
                  'ratings', 'reviews']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'products']