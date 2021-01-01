from behave import *
from selenium import webdriver
from time import sleep

@given(u'Launch the browser')
def Launch_Browser(context):
    # raise NotImplementedError(u'STEP: Given Launch the browser')
    context.driver=webdriver.Chrome()
    # sleep(2)

@when(u'Open Amazon Home Page')
def Home_Page(context):
    # raise NotImplementedError(u'STEP: When Open Amazon Home Page')
    context.driver.get("https://www.amazon.in/")
    # sleep(2)


@then(u'Click First Accounts')
def Account(context):
    # raise NotImplementedError(u'STEP: Then Click on Accounts')
    context.driver.find_element_by_xpath("//a[@id='nav-link-accountList']").click()
    # sleep(2)

@then(u'Enter the Email {user}')
def Email(context, user):
    # raise NotImplementedError(u'STEP: Then Enter the Email')
    context.driver.find_element_by_id("ap_email").send_keys(user)
    # sleep(2)


@then(u'Click on Continue')
def First_Next(context):
    # raise NotImplementedError(u'STEP: Then Click on Continue')
    context.driver.find_element_by_id("continue").click()
    # sleep(2)

@then(u'Enter the Password {pwd}')
def Password(context, pwd):
    # raise NotImplementedError(u'STEP: Then Enter the password')
    context.driver.find_element_by_id("ap_password").send_keys(pwd)
    # sleep(2)

@then(u'Click on Login')
def Second_Next(context):
    # raise NotImplementedError(u'STEP: Then Click on signin')
    context.driver.find_element_by_id("signInSubmit").click()
    sleep(20)

@then(u'Click Second Accounts')
def Accounts(context):
    context.driver.find_element_by_xpath("//a[@id='nav-link-accountList']").click()
    # sleep(2)

@then(u'Click the Orders')
def Orders(context):
    context.driver.find_element_by_xpath("//body[@class='a-aui_72554-c a-aui_mm_desktop_exp_291916-c a-aui_mm_desktop_launch_291918-c a-aui_mm_desktop_targeted_exp_291928-t1 a-aui_mm_desktop_targeted_launch_291922-t1 a-aui_pci_risk_banner_210084-c a-aui_perf_130093-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_tnr_v2_180836-c']/div[@id='a-page']/div[@class='a-container']/div[@class='a-section ya-personalized']/div[2]/div[1]/a[1]/div[1]/div[1]").click()
    # assert text =="Your Orders"
    # sleep(2)

# @then(u'Click Third Account')
# def Account(context):
#     context.driver.find_element_by_xpath("//span[@class='nav-line-2 nav-short-width']").click()
#     sleep(5)

@then(u'Sign Out')
def Sign_Out(context):
    context.driver.find_element_by_id("//a[@id='nav-item-signout']").click()
    # text = context.driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").text
    # assert text == "Sign Out"
    # sleep(2)
# Amzon Login For Indian Server

@then(u'Browser Closing')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then Browser Closing')
    context.driver.close()
