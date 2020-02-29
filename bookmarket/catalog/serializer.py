from rest_framework import serializers

from .models import *

class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['first_name','last_name','age','books','url']



class BookSerializer(serializers.ModelSerializer):

    # author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = ['title','genre','pub_date','author']