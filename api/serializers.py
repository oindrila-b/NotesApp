from rest_framework import serializers
from base.models import Note
from base.models import VersionHistory
from base.models import UserNoteModel


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class UserNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNoteModel
        fields = '__all__'


class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionHistory
        fields = '__all__'
