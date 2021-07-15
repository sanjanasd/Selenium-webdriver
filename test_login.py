from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from selenium.webdriver.chrome.options import Options

def test_login_automation():
    USERNAME = input("Enter in your username:")
    PASSWORD = getpass("Enter your password:")

    test_login_automation.driver = webdriver.Chrome(ChromeDriverManager().install())
    test_login_automation.driver.get("http://demo.guru99.com/insurance/v1/index.php")

    user_input = test_login_automation.driver.find_element_by_id("email")
    user_input.send_keys(USERNAME)

    password_input = test_login_automation.driver.find_element_by_id("password")
    password_input.send_keys(PASSWORD)

    login_button = test_login_automation.driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/input")
    login_button.click()

if __name__=="__main__":
    test_login_automation()    
    if len(test_login_automation.driver.find_elements_by_xpath("/html/body/div[3]/div/div[1]/h2")):
        print("Pass")
    else: 
        print("Fail")






