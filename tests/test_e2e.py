import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logging()
        prod = 'Blackberry'
        final_msg = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")

        products = checkOutPage.getCardTitle()
        for product in products:
            if prod == product.text:
                product.checkOutPage.addToCard.click()
                log.info("adding item to cart")

        checkOutPage.checkoutTab().click()

        confirmPage = checkOutPage.checkoutButton()

        confirmPage.locationTab().send_keys("ind")
        log.info("entering country name")

        self.verifyLinkPresence("India")

        confirmPage.clickonCountry().click()

        confirmPage.clickonCheckbox().click()

        confirmPage.clickOnSubmit().click()

        success_text = confirmPage.successMessage().text
        log.info("Text received from application"+ success_text)
        print(success_text)
        print(final_msg)
        assert final_msg in success_text
        print("git exersice in gitDemo")
        print("hello")

