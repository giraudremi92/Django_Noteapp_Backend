from todo.models import Todo
from django.test import TestCase

from todo.models import Todo

class TodoTestCases(TestCase):

    def test_create_todo(self):


        nbr_of_todos = Todo.objects.count()
        print(nbr_of_todos)
