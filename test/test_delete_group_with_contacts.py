# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_delete_group_with_contacts(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group(Group(name="my group"))
    old_list = app.groups.get_group_list()
    l = len (old_list) - 1
    index= random.randint(0, l)
    app.groups.delete_group_with_contacts(index)
    assert len(old_list) - 1 == app.groups.count()
    new_list = app.groups.get_group_list()
    old_list.pop(index)
    assert sorted(old_list, key=Group.name_group) == sorted(new_list, key=Group.name_group)