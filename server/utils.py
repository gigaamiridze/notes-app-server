from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

def get_note_list(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

def get_note_detail(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def create_note(request):
    data = request.data['body']
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def update_note(request, id):
    data = request.data['body']
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response('Note was deleted!')
