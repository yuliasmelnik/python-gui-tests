# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_modify_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group(name="my group")
    old_list = app.groups.get_group_list()
    group = Group(name="Modify group")
    l = len (old_list) - 1
    index= random.randint(0, l)
    app.groups.modify_group(index, group)
    assert len(old_list) == app.groups.count()
    new_list = app.groups.get_group_list()
    old_list[index] = str(group)
    assert sorted(old_list) == sorted(new_list)