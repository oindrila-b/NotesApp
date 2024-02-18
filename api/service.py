from base.models import Note
from .serializers import NoteSerializer


def getAllNotesFromDB():
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return serializer.data


def getNoteById(note_id):
    notes = Note.objects.all().filter(id=note_id)
    serializer = NoteSerializer(notes, many=True)
    return serializer.data


def addNewNote(data):
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data


def updateNoteData(note_data, note_id):
    note = Note.objects.filter(id=note_id).first()
    serializer = NoteSerializer(note, data=note_data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return serializer.data
