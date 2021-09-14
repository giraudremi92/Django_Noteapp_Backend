from django.contrib import admin

from todo.models import Todo

class TodoInline(admin.TabularInline):

    model = Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    
    list_display = ('title','description','color')
    search_fields = ('title',)
