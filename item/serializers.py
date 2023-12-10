from rest_framework import serializers
from .models import Item, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'course', 'category', 'pdf')

class ItemGetSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.name')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = ('id', 'user', 'author', 'name', 'description', 'course', 'category', 'pdf', 'created', 'updated')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('item', 'user', 'body')

class CommentGetSerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source='user.name')
    author = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comment
        fields = ('id', 'item', 'user', 'author', 'body')


class CommentPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body')