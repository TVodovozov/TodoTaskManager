import graphene
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = "__all__"


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)


class Query(graphene.ObjectType):
    all_todos = graphene.List(ToDoType)


def resolve_all_projects(root, info):
    return Project.objects.all()


def resolve_all_todos(root, info):
    return ToDo.objects.all()


schema = graphene.Schema(query=Query)
