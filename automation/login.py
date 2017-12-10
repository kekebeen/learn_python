from page import Page

c = Page('chrome')
loginButtonXpath = "//input[@value='Log In']"

c.find_by_id_and_click("email", "test@mail.com")
c.find_by_id_and_click("pass", "test")
c.button_by_xpath_click(loginButtonXpath)
c.tearDown()

