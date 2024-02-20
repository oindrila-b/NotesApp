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
    print(notes)
    if notes is None:
        return -1
    else:
        serializer = NoteSerializer(notes, many=True)
        return serializer.data


def addNewNote(data):
    serializer = NoteSerializer(data=data)
    # create another notes object and then store it
    if serializer.is_valid():
        serializer.save()
        new_version = VersionHistory.objects.create(note_id=serializer.data['id'], version=serializer.data['version'])
        new_version.notes.append(serializer.data)
        new_version.save()
        print(new_version)
    else:
        return serializer.errors
    return 1


def updateNoteData(note_data, note_id):
    note = Note.objects.filter(id=note_id).first()
    print(note_data)
    if note is None:
        return -1
    note_data['version'] = note.version + 1
    print(note_data)
    serializer = NoteSerializer(note, data=note_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        versions = VersionHistory.objects.get(note_id=serializer.data['id'])
        print(versions.note_id)
        versions.notes.append(serializer.data)
        versions.save()
    else:
        return -1
    return 1


def deleteAllRecords():
    Note.objects.all().delete()
    VersionHistory.objects.all().delete()
    return "Success"


def deleteNoteByID(note_id):
    note = Note.objects.all().filter(id=note_id).first()
    print(note)
    if note is None:
        return -1
    else:
        note.delete()
        return "Success"


def getAllVersionsNotes():
    notes = VersionHistory.objects.all()
    version_serializer = VersionHistorySerializer(notes, many=True)
    return version_serializer.data


def getVersionNotesByID(id):
    notes = VersionHistory.objects.all().filter(note_id=id)
    print(notes)
    if notes is None:
        return -1
    else:
        version_serializer = VersionHistorySerializer(notes, many=True)
        return version_serializer.data
