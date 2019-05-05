from django.http import Http404
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer


class TaskListApiView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListDetail(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        task_list_serializer = TaskListSerializer(task_list)
        return Response({
            'task_list': task_list_serializer.data,
         })

    def delete(self,request, pk):
        task_list = self.get_object(pk)
        task_list_serializer = TaskListSerializer(task_list)
        task_list.delete()
        return Response(task_list_serializer.data)

    def put(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    serializer = UserSerializer(user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': serializer.data
    })



class TaskApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    serializer_class = TaskSerializer









