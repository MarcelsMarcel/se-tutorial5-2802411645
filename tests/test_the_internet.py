from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

# def test_open_browser():
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/var/lib/flatpak/app/com.brave.Browser/current/active/export/bin/com.brave.Browser"
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     service = BraveService(
#         ChromeDriverManager(chrome_type=ChromeType.BRAVE, driver_version="148").install()
#     )
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("https://the-internet.herokuapp.com/")

#     driver.quit()

# def test_get_element():
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/var/lib/flatpak/app/com.brave.Browser/current/active/export/bin/com.brave.Browser"
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     service = BraveService(
#         ChromeDriverManager(chrome_type=ChromeType.BRAVE, driver_version="148").install()
#     )
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("https://the-internet.herokuapp.com/")

#     heading = driver.find_element(By.TAG_NAME, "h1")
#     assert heading.text == "Welcome to the-internet"

#     import time
#     time.sleep(10)
#     driver.quit()

# def test_click_button():
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/var/lib/flatpak/app/com.brave.Browser/current/active/export/bin/com.brave.Browser"
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     service = BraveService(
#         ChromeDriverManager(chrome_type=ChromeType.BRAVE, driver_version="148").install()
#     )
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

#     driver.find_element(By.XPATH, "//*[@id=\"content\"]/div/button").click()
#     delete_button = driver.find_element(By.CLASS_NAME, "added-manually")
#     assert delete_button.is_displayed()

#     import time
#     time.sleep(10)
#     driver.quit()

def test_login_correct():
    options = webdriver.ChromeOptions()
    options.binary_location = "/var/lib/flatpak/app/com.brave.Browser/current/active/export/bin/com.brave.Browser"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = BraveService(
        ChromeDriverManager(chrome_type=ChromeType.BRAVE, driver_version="148").install()
    )
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, "//*[@id=\"login\"]/button/i").click()

    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text

    import time
    time.sleep(10)
    driver.quit()

def test_login_incorrect():
    options = webdriver.ChromeOptions()
    options.binary_location = "/var/lib/flatpak/app/com.brave.Browser/current/active/export/bin/com.brave.Browser"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = BraveService(
        ChromeDriverManager(chrome_type=ChromeType.BRAVE, driver_version="148").install()
    )
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("sahdsahdsah")
    driver.find_element(By.XPATH, "//*[@id=\"login\"]/button/i").click()

    error_message = driver.find_element(By.ID, "flash")
    assert "Your password is invalid!" in error_message.text

    import time
    time.sleep(10)
    driver.quit()