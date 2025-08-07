# -*- coding: utf-8 -*-
from model.group import Group
from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def test_add_group(app):
    old_list = app.groups.get_group_list()
    file = (os.path.join(project_dir, 'groups.xlsx'))
    xl = CreateObject("Excel.Application")
    xl.Visible = 1
    wb = xl.Workbooks.Open(file)
    worksheet = wb.Sheets[1]
    for row in range(1, 11):
        text = worksheet.Cells[row, 1].Value()
        group= Group(name = text)
        app.groups.add_new_group(group)
        old_list.append(group)
    xl.Quit()
    new_list = app.groups.get_group_list()
    assert sorted(old_list, key=Group.name_group) == sorted(new_list, key=Group.name_group)