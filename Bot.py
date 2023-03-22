from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SeleniumBot:
    def __init__(self, undetected: bool = False, cookies=False, user_agent=False):
        
        if type(undetected) != bool:
            raise TypeError("Variable 'undetected' must be of boolean type.")

        if not undetected:
            self.driver = webdriver.Chrome()
        else:
            self.driver = uc.Chrome()

        if cookies:

            for cookie in cookies:
                self.driver.add_cookie(cookie)

        if user_agent:
            options = Options()
            options.add_argument(f"user-agent={user_agent}")

            self.driver = uc.Chrome(options=options)
        
        self.actions = ActionChains(self.driver)

        self.commands = self.Commands(self)
            
    def open_page(self, url):
        self.driver.get(url)

    def close_page(self):

        self.driver.quit()

    def fill_input(self, by, locator, text, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
        element.clear()
        element.send_keys(text)

    def find_element(self, by, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def find_visible_element(self, by, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def find_elements(self, by, locator, timeout=30):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )

        return elements

    def click_button(self, by, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def extract_text(self, by, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element.text

    class Commands:

        def __init__(self, classe_pai):
            self.classe_pai = classe_pai

        def enter(self):
            self.classe_pai.actions\
            .send_keys(Keys.ENTER)

            self.classe_pai.actions.perform()

        def ctrl_shift_e(self):
            self.classe_pai.actions \
            .key_down(Keys.CONTROL)\
            .key_down(Keys.SHIFT)\
            .send_keys("E")

            self.classe_pai.actions.perform()

        def ctrl_c(self):
            self.classe_pai.actions \
            .key_down(Keys.CONTROL)\
            .send_keys("C")

            self.classe_pai.actions.perform()

        def ctrl_v(self):

            self.classe_pai.actions \
            .key_down(Keys.CONTROL)\
            .send_keys("V")

            self.classe_pai.actions.perform()

        def ctrl_a(self):
            self.classe_pai.actions \
            .key_down(Keys.CONTROL)\
            .send_keys("A")

            self.classe_pai.actions.perform()
        def alt_enter(self):
            self.classe_pai.actions \
            .key_down(Keys.ALT)\
            .key_down(Keys.ENTER)

            self.classe_pai.actions.perform()