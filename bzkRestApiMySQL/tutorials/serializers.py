from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from tutorials.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    class Model:
        model = Tutorial
        fields = ('id', 'title', 'description', 'published')