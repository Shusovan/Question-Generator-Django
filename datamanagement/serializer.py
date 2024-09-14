# Serializers define the API representation.
from rest_framework import serializers
from .models import Question, UploadDocuments, UploadString, SubjectRegister

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ("id", "row_created")


class UploadDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDocuments
        fields = "__all__"
        read_only_fields = ("id", "row_created")


class UploadStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadString
        fields = "__all__"
        read_only_fields = ("id", "row_created")


class SubjectRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRegister
        fields = "__all__"
        read_only_fields = ("id", "row_created", "index_location")