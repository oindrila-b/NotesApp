from rest_framework.response import Response
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
    return Response(new_data)


@api_view(['PATCH'])
def updateNote(request, id):
    updated_note = updateNoteData(request.data, id)
    return Response(updated_note)

