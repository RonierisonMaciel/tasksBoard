from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Task
from rest_framework import viewsets
from .serializer import BoardSerializer, TaskSerializer
from .forms import TaskForm, BoardForm
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.datastructures import MultiValueDictKeyError


def index(request):

    context = {"boards": Board.objects.all()}
    return render(request, "index.html", context)


def board_page(request, board_id: int):

    board = get_object_or_404(Board, id=board_id)

    context = {
        "board": board,
        "pending_tasks": Task.objects.all()
        .filter(board_id=board_id)
        .filter(status="Pending"),
        "doing_tasks": Task.objects.all()
        .filter(board_id=board_id)
        .filter(status="Doing"),
        "done_tasks": Task.objects.all()
        .filter(board_id=board_id)
        .filter(status="Done"),
        "status_list": Task.status_list,
    }
    return render(request, "board.html", context)


def new_task(request, board_id):

    form = TaskForm(request.POST)

    if form.is_valid():
        form.save(commit=True)

    return redirect("boardpage", board_id=board_id)


def edit_task(request):

    id = request.POST["id"]

    task = get_object_or_404(Task, id=id)

    task.status = request.POST["status"]
    task.save()

    return redirect("boardpage", board_id=task.board_id.id)


def new_board(request):
    form = BoardForm(request.POST)

    if form.is_valid():
        form.save(commit=True)

    return redirect("homepage")


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False)
    def pending(self, request):
        queryset = Task.objects.all().filter(status="pending")
        serializer = TaskSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @action(detail=False)
    def doing(self, request):
        queryset = Task.objects.all().filter(status="doing")
        serializer = TaskSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @action(detail=False)
    def done(self, request):
        queryset = Task.objects.all().filter(status="done")
        serializer = TaskSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)
