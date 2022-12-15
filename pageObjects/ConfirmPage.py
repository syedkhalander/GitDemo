from selenium.webdriver.common.by import By


class ConfirmPage:
    locationTabVar = (By.CSS_SELECTOR, "#country")
    clickOnCountry = (By.LINK_TEXT, "India")
    clickOnCheckBox = (By.XPATH, "//div[@class ='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    successMsg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
    def locationTab(self):
        return self.driver.find_element(*ConfirmPage.locationTabVar)

    # self.driver.find_element(By.LINK_TEXT, "India").click()
    def clickonCountry(self):
        return self.driver.find_element(*ConfirmPage.clickOnCountry)

    # self.driver.find_element(By.XPATH, "//div[@class ='checkbox checkbox-primary']").click()
    def clickonCheckbox(self):
        return self.driver.find_element(*ConfirmPage.clickOnCheckBox)

    # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    def clickOnSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    # success_text = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.successMsg)
