from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ['id','owner', 'title', 'review_body', 'movie', 'created']


class MovieSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_url','trailer_url', 'year_released', 'reviews']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True, view_name='review-detail', read_only=True)

    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('id', 'username', 'reviews', 'email', 'password')