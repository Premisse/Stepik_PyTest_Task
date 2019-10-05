import time


def test_check_button_exists(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    # to check uncomment this line
    # time.sleep(30)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "Button not found"



