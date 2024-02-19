from base.models import Note
from .serializers import NoteSerializer
from base.models import VersionHistory
from .serializers import VersionHistorySerializer


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
    VersionHistory.objects.all().delete()
    if serializer.is_valid():
        serializer.save()
    else:
        return serializer.errors
    return '1'


def updateNoteData(note_data, note_id):
    note = Note.objects.filter(id=note_id).first()
    print(note_data)
    note_data['version'] = note.version + 1
    print(note_data)
    serializer = NoteSerializer(note, data=note_data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return '-1'
    return '1'


def deleteAllRecords():
    Note.objects.all().delete()
    return "Success"


def deleteNoteByID(note_id):
    Note.objects.filter(id=note_id).delete()
    return "Success"


def getAllVersionsNoteByID():
    notes = VersionHistory.objects.all()
    version_serializer = VersionHistorySerializer(notes, many=True)
    return version_serializer.data[0]['notes']
