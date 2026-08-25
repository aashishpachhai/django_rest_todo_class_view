from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializers
from todo.models import Todo
from django.http import Http404
# Create your views here.
class Todos(APIView):

    def get(self,request):
        todo=Todo.objects.all()
        serial=TodoSerializers(todo,many=True)
        return Response(serial.data,status=200)

    def post(self,request):
        todo=TodoSerializers(data=request.data)
        if todo.is_valid():
            todo.save()
            return Response(todo.data,status=200)
        else:
            return Response(todo.errors,status=500)

class TodoDetail(APIView):

    def getDeatil(self,id):
        try:
            todo=Todo.objects.get(pk=id)
            return todo
        except Todo.DoesNotExist:
            return Http404

    def get(self,request,id):
        td=self.getDeatil(id)
        serial=TodoSerializers(td)
        return Response(serial.data,status=200)
    
    def put(self,request,id):
        td=self.getDeatil(id)
        t=TodoSerializers(td,data=request.data)
        if t.is_valid():
            t.save()
            return Response(t.data,status=200)
        else:
            return Response(t.errors,status=500)

    
    def delete(self,request,id):
        t=self.getDeatil(id)
        t.delete()
        return Response(status=200)
            