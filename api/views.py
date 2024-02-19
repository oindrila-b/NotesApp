from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .service import *


@api_view(['GET'])
def getAllNotes(request):
    all_notes = getAllNotesFromDB()
    return Response(all_notes)


@api_view(['GET'])
def getNoteByID(request, id):
    note = getNoteById(id)
    return Response(note)


@api_view(['POST'])
def addNote(request):
    new_data = addNewNote(request.data)
    if new_data == '1':
        return Response("Successfully Created New Note", status=status.HTTP_200_OK)
    else:
        return Response(new_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateNote(request, id):
    updated_note = updateNoteData(request.data, id)
    return Response(updated_note)


@api_view(['DELETE'])
def deleteAll(request):
    deleteAllRecords()
    return Response("Deleted")


@api_view(['DELETE'])
def deleteByID(request, id):
    deleteNoteByID(id)
    return Response("Deleted Note")


@api_view(['GET'])
def getNotesVersionHistory(request):
    versions = getAllVersionsNoteByID()
    print(versions)
    return Response(versions)
