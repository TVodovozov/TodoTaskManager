from graphene import ID, Boolean, Field, List, Mutation, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo
from userapp.models import User


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class TodoObjectType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = "__all__"


class Query(ObjectType):
    users = List(UserObjectType)
    projects = List(ProjectObjectType)
    todos = List(TodoObjectType)
    users_by_name = List(UserObjectType, name=String(default_value=""))
    user_by_id = Field(UserObjectType, id=ID(required=True))
    projects_by_name = List(ProjectObjectType, name=String(default_value=""))

    def resolve_users_by_name(self, info, name):
        return User.objects.filter(first_name__contains=name)

    def resolve_projects(self, info):
        return Project.objects.all()

    def resolve_todos(self, info):
        return ToDo.objects.all()

    def resolve_projects_by_name(self, info, name):
        return Project.objects.filter(name__contains=name)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user_by_id(self, info, id):
        return User.objects.get(id=id)


class TodoMutation(Mutation):
    class Arguments:
        id = ID()
        is_active = Boolean(required=True)

    todo = Field(TodoObjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        todo = ToDo.objects.get(id=kwargs.get("id"))
        todo.is_active = kwargs.get("is_active")
        todo.save()
        return cls(todo=todo)


class Mutation(ObjectType):
    update_todo = TodoMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
