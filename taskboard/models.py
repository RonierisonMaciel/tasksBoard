from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Task(models.Model):

    status_list = [
        ("Pending", "Pending"),
        ("Doing", "Doing"),
        ("Done", "Done"),
    ]

    board_id = models.ForeignKey(
        Board, on_delete=models.CASCADE, null=False, blank=False
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=status_list, default="Pending"
    )

    def __str__(self):
        return self.title
