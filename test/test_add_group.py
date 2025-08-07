# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_list = app.groups.get_group_list()
    group = Group(name="my group")
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=Group.name_group) == sorted(new_list, key=Group.name_group)