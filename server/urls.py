from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('notes', views.get_notes, name='notes'),
    path('notes/<str:id>', views.get_note_by_id, name='note'),
    path('notes/<str:id>/update', views.update_note, name='update_note'),
    path('notes/<str:id>/delete', views.delete_note, name='delete_note'),
]
