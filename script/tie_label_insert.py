# coding=utf-8
from webuser.models import *
from api.v1.student.views import tie_label_table


def insert():
    for label_name in tie_label_table:
        label, result = Label.objects.get_or_create(name=label_name)
        label.group = Label.TIE
        label.save()