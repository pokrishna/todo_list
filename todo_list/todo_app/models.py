from django.db import models
#from django.utils.timezone import utc
class todo_list(models.Model):
    Title=models.CharField(max_length=120)
    Description=models.CharField(max_length=120)
    DateTime_of_todo_task=models.DateTimeField(auto_now=False,auto_now_add=False)
    Status_Choices=(
    ("progress","progress"),
    ("completed","completed"),
    ("pending","pending"),
    )
    Status=models.CharField(max_length=25,choices=Status_Choices)
    Created=models.DateTimeField(auto_now_add=True)
    Modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
