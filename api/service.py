from base.models import Note
from base.models import UserNoteModel
from .serializers import NoteSerializer
from base.models import VersionHistory
from .serializers import VersionHistorySerializer, UserNoteSerializer


def getAllNotesFromDB(user):
    notes = UserNoteModel.objects.all().filter(name=user)
    serializer = UserNoteSerializer(notes, many=True)
    return serializer.data


def getNoteById(note_id):
    notes = UserNoteModel.objects.all().filter(id=note_id)
    print(notes)
    if notes is None:
        return -1
    else:
        serializer = NoteSerializer(notes, many=True)
        return serializer.data


def addNewNote(user, data):
    serializer = NoteSerializer(data=data)
    # create another notes object and then store it
    if serializer.is_valid():
        serializer.save()
        new_version = VersionHistory.objects.create(note_id=serializer.data['id'], version=serializer.data['version'])
        new_version.notes.append(serializer.data)
        new_version.save()
        if UserNoteModel.objects.all().filter(name=user).first() is None:
            new_user_note_model = UserNoteModel.objects.create(name=user)
            new_user_note_model.notes.append(serializer.data)
            new_user_note_model.save()
        else:
            old_user = UserNoteModel.objects.get(name=user)
            old_user.notes.append(serializer.data)
            old_user.save()
    else:
        return serializer.errors
    return 1


def updateNoteData(note_data, note_id, user):
    note = Note.objects.filter(id=note_id).first()
    if note is None:
        return -1
    note_data['version'] = note.version + 1
    print(note_data)
    serializer = NoteSerializer(note, data=note_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        versions = VersionHistory.objects.get(note_id=serializer.data['id'])
        versions.notes.append(serializer.data)
        versions.save()
        updated_user_note = UserNoteModel.objects.get(name=user)
        print(updated_user_note.notes)
        for i in range(len(updated_user_note.notes)):
            var = updated_user_note.notes[i]
            if var['id'] == serializer.data['id']:
                var = serializer.data
                print(var)
                updated_user_note.notes[i] = var
                print(updated_user_note.notes[i])
                updated_user_note.save()
                break
    else:
        return -1
    return 1


def deleteAllRecords():
    UserNoteModel.objects.all().delete()
    VersionHistory.objects.all().delete()
    Note.objects.all().delete()
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
