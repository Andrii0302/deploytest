from rest_framework import serializers
from .models import Item, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comment
        fields = ('item', 'user', 'body')


class CommentPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body')