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
    if note == -1:
        return Response("Unable to find note with the given ID", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(note, status=status.HTTP_200_OK)


@api_view(['POST'])
def addNote(request):
    response = addNewNote(request.data)
    if response == 1:
        return Response("Successfully Created New Note", status=status.HTTP_200_OK)
    else:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateNote(request, id):
    response = updateNoteData(request.data, id)
    if response == -1:
        return Response('Unable to update note with the given id,try sending the correct id',
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Updated Note Successfully", status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteAll(request):
    deleteAllRecords()
    return Response("Deleted", status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteByID(request, id):
    message = deleteNoteByID(id)
    if message == -1:
        return Response("Unable to find note with given ID", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def getNotesVersionHistory(request):
    versions = getAllVersionsNotes()
    print(versions)
    return Response(versions)


@api_view(['GET'])
def getNotesVersionHistoryByID(request, id):
    versions = getVersionNotesByID(id)
    print(versions)
    if versions == -1:
        return Response("Unable to find version with the given not ID, try entering a valid ID",
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(versions, status=status.HTTP_200_OK)
