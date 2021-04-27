from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver import FirefoxOptions


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["user.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        cls.driver = webdriver.Firefox(firefox_options=opts)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        super().tearDownClass()

    def test_login(self):
        self.driver.get("%s%s" % (self.live_server_url, "/accounts/login/"))

        username_input = self.driver.find_element_by_name("login")
        username_input.send_keys("loggeduser")

        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("!M4dygH3ZWfd0214U59OR9nlwsRJ94HUZtvQciG8y")
        self.driver.find_element_by_name("sign").click()
