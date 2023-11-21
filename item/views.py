from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import Http404


#APi for category

class CategoryAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CategorySerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def get(self, request):
        categorys = get_list_or_404(Category)
        serializer = self.serializer_class(categorys, many=True)
        return Response(serializer.data)
    
class CategoryIDView(APIView):
    serializer_class = CategorySerializer

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = self.serializer_class(instance=category, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            category = get_object_or_404(Category, id=pk)
            category.delete()
            return Response('Category was deleted!')
        except Http404:
                # Handle the case where the Category with the given id does not exist
                return Response('Category with the specified ID does not exist.', status=404)











# API for items

class ItemAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ItemSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def get(self, request):
        items = get_list_or_404(Item)
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)


class ItemIDView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, pk):
        items = get_object_or_404(Item, id=pk)
        serializer = ItemSerializer(items, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        serializer = self.serializer_class(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            item = get_object_or_404(Item, id=pk)
            item.delete()
            return Response('Item was deleted!')
        except Http404:
                # Handle the case where the Category with the given id does not exist
                return Response('Item with the specified ID does not exist.', status=404)
    
