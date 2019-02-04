class GroupHelper:

    def __init__(self, fixt):
        self.fixt = fixt

    def create(self, group):
        wd = self.fixt.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.fixt.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.fixt.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.fixt.wd
        self.open_groups_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, edit_group):
        wd = self.fixt.wd
        self.open_groups_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #click edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(edit_group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(edit_group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(edit_group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
