from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    addToCard = (By.XPATH, "div/button")
    checkOutTab = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOutButton = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    #find_element(By.XPATH, "div/button")
    def getAddToCard(self):
        return self.driver.find_element(*CheckOutPage.addToCard)

    # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    def checkoutTab(self):
        return self.driver.find_element(*CheckOutPage.checkOutTab)

    # self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
    def checkoutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        # confirmPage = ConfirmPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
