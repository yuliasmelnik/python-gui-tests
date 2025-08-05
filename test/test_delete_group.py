# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group(name="my group")
    old_list = app.groups.get_group_list()
    l = len (old_list) - 1
    index= random.randint(0, l)
    app.groups.delete_group(index)
    assert len(old_list) - 1 == app.groups.count()
    new_list = app.groups.get_group_list()
    old_list.pop(index)
    assert sorted(old_list) == sorted(new_list)