from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_note_list, get_note_detail, create_note, update_note, delete_note

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET', 'POST'])
def get_notes(request):
    if request.method == 'GET':
        return get_note_list(request)

    if request.method == 'POST':
        return create_note(request)

@api_view(['GET', 'PUT', 'DELETE'])
def get_note(request, id):
    if request.method == 'GET':
        return get_note_detail(request, id)

    if request.method == 'PUT':
        return update_note(request, id)

    if request.method == 'DELETE':
        return delete_note(request, id)
