import graphene
from graphene_django import DjangoObjectType
from .models import Task
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import TaskSerializer

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    def resolve_all_tasks(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication required!")
        return Task.objects.filter(assigned_to=user)

schema = graphene.Schema(query=Query)
