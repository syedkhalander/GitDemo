from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    genderSelect = (By.ID, "exampleFormControlSelect1")
    radioSelect = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMsg = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        # checkOutPage = CheckOutPage(self.driver)
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    #self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("syed")
    def passingName(self):
        return self.driver.find_element(*HomePage.name)

    #self.driver.find_element(By.NAME, "email").send_keys("syedkhalander.l")
    def passingEmail(self):
        return self.driver.find_element(*HomePage.email)

    #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234567")
    def passingPassword(self):
        return self.driver.find_element(*HomePage.password)

    #self.driver.find_element(By.ID, "exampleCheck1").click()
    def clickOnCheckbox(self):
        return self.driver.find_element(*HomePage.checkBox)

    #Select(self.driver.find_element(By.ID, "exampleFormControlSelect1")
    def selectGender(self):
        return self.driver.find_element(*HomePage.genderSelect)

    #self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
    def selectRadio(self):
        return self.driver.find_element(*HomePage.radioSelect)

    #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    def clickOnSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    #self.driver.find_element(By.CLASS_NAME, "alert-success")
    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)