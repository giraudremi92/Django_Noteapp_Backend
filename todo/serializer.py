from rest_framework_json_api import serializers

from todo.models import Todo


class Todoserializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"
        
