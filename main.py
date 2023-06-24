from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    browser = webdriver.Firefox(executable_path=r"./geckodriver")
    browser.get('https://tevis.ekom21.de/stdar/?lang=de_VS&rs')
    cookie_button_yes = browser.find_element(By.XPATH, '//*[@id="cookie_msg_btn_yes"]')
    cookie_button_yes.click()
    select_authority = browser.find_element(By.XPATH, '//*[@id="buttonfunktionseinheit-7"]')
    select_authority.click()
    select_concern = browser.find_element(By.XPATH, '//*[@id="header_concerns_accordion-229"]')
    select_concern.click()
    add_one_button = browser.find_element(By.XPATH, '//*[@id="button-plus-1981"]')
    add_one_button.click()
    further_button = browser.find_element(By.XPATH, '//*[@id="WeiterButton"]')
    further_button.click()
    accept_note = browser.find_element(By.XPATH, '//*[@id="OKButton"]')
    accept_note.click()
    seven_o_clock = browser.find_element(By.XPATH, '/html/body/main/div[1]/div[6]/div[1]/table/tbody/tr[1]/td[1]/form/button')
    block_appointment = browser.find_element(By.XPATH, '/html/body/main/div[1]/div[6]/div[1]/table/tbody/tr[5]/td[8]/button')
    a ='//*[@id="ui-id-1"]'
    a = '//*[@id="ui-id-2"]'
    a = block_appointment.get_attribute("title")
    c = block_appointment.get_attribute("disabled")
    aa = seven_o_clock.get_attribute("disabled")
    b = block_appointment.get_property("title")

    d = ""