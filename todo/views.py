from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from todo.models import Todo
from todo.serializer import Todoserializer

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = Todoserializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,) 
