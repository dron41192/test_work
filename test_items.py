import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_and_any_language(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_xpath("//button[@value]")