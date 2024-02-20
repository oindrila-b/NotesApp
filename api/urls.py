from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.getAllNotes),
    path('notes/create', views.addNote),
    path('notes/<int:id>', views.getNoteByID),
    path('notes/update/<int:id>', views.updateNote),
    path('notes/delete', views.deleteAll),
    path('notes/delete/<int:id>', views.deleteByID),
    path('versions', views.getNotesVersionHistory),
    path('versions/<int:id>', views.getNotesVersionHistoryByID)
]
