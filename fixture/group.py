from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        group_list = []
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        #group_list = [node.text() for node in root.children()]
        for node in root.children():
            text = node.text()
            group_list.append(Group(name= text))
        self.close_group_editor()
        return group_list

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group)
        input.type_keys("/n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def select_group(self, index):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        tree.GetItem((0, index)).Click()

    def delete_group(self, index):
        self.open_group_editor()
        self.select_group(index)
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def delete_group_with_contacts(self, index):
        self.open_group_editor()
        self.select_group(index)
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def modify_group(self, index, group):
        self.open_group_editor()
        self.select_group(index)
        self.group_editor.window(auto_id="uxEditAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group)
        input.type_keys("/n")
        self.close_group_editor()


    def count(self):
        self.get_group_list()
        return len(self.get_group_list())