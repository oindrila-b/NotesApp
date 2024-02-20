from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .service import *
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

logged_user = "name"


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/notes')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
@api_view(['GET'])
def getAllNotes(request):
    print(request.user.username)
    all_notes = getAllNotesFromDB(request.user.username)
    return Response(all_notes)


@login_required(login_url='/login')
@api_view(['GET'])
def getNoteByID(request, id):
    note = getNoteById(id)
    if note == -1:
        return Response("Unable to find note with the given ID", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(note, status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['POST'])
def addNote(request):
    response = addNewNote(request.user.username, request.data)
    if response == 1:
        return Response("Successfully Created New Note", status=status.HTTP_200_OK)
    else:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='/login')
@api_view(['PATCH'])
def updateNote(request, id):
    response = updateNoteData(request.data, id, request.user.username)
    if response == -1:
        return Response('Unable to update note with the given id,try sending the correct id',
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Updated Note Successfully", status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['DELETE'])
def deleteAll(request):
    deleteAllRecords()
    return Response("Deleted", status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['DELETE'])
def deleteByID(request, id):
    message = deleteNoteByID(id)
    if message == -1:
        return Response("Unable to find note with given ID", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(message, status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['GET'])
def getNotesVersionHistory(request):
    versions = getAllVersionsNotes()
    print(versions)
    return Response(versions)


@login_required(login_url='/login')
@api_view(['GET'])
def getNotesVersionHistoryByID(request, id):
    versions = getVersionNotesByID(id)
    print(versions)
    if versions == -1:
        return Response("Unable to find version with the given not ID, try entering a valid ID",
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(versions, status=status.HTTP_200_OK)
