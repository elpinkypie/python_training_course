

def test_delete_first_group(fixt):
    fixt.session.login(username="admin", password="secret")
    fixt.contact.delete_first_contact()
    fixt.session.logout()
