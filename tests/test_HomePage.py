import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.get_logging()
        homePage = HomePage(self.driver)

        homePage.passingName().send_keys(getData["firstname"])
        log.info("First name" + getData["firstname"])
        time.sleep(2)
        homePage.passingEmail().send_keys(getData["lastname"])
        homePage.passingPassword().send_keys("1234567")
        homePage.clickOnCheckbox().click()
        self.selectDropDown(homePage.selectGender(), getData["gender"])
        homePage.selectRadio().click()
        homePage.clickOnSubmit().click()

        msg = homePage.getSuccessMsg().text
        print(msg)
        assert "Success" \
               "" in msg
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("again")
        self.driver.refresh()
        print("git exersice in gitDemo")

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
