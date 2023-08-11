from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    title = serializers.CharField(max_length=200)
    isbn = serializers.CharField(max_length=13)
    genre = serializers.CharField(max_length=20)


class AuthorSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=20)
