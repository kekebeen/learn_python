from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Page():
    def __init__(self, browser):
      self.driver = None
      if(browser == 'chrome'):
        self.driver = webdriver.Chrome()
      else:
        self.driver = webdriver.Firefox()

      self.driver.get("https://wwww.facebook.com")

    def find_by_id_and_click(self, id, value):
      id = id
      el = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(id))
      el.clear()
      el.send_keys(value)

    def button_by_xpath_click(self, xpath):
      el = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(xpath))
      el.click()

    def test_login(self):
        fb_uname = "Your Email Here"
        fb_upasee = "Your Password Here"

        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpath = "//input[@value='Log In']"

        emailFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(fb_uname)

        passFieldElement.clear()
        passFieldElement.send_keys(fb_upasee)

        loginButtonElement.click()


    def tearDown(self):
        self.driver.quit()

