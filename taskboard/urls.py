from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from .views import (
    edit_task,
    index,
    board_page,
    BoardViewSet,
    TasksViewSet,
    new_task,
    new_board,
)

router = routers.DefaultRouter()
router.register(r"boards", BoardViewSet)
router.register(r"tasks", TasksViewSet)


urlpatterns = [
    path("", index, name="homepage"),
    path("new-board", new_board, name="new-board"),
    path("<int:board_id>", board_page, name="boardpage"),
    path("<int:board_id>/new-task", new_task, name="new-task"),
    path("edit-task-status/", edit_task, name="edit-task"),
    path("api/", include(router.urls)),
]
