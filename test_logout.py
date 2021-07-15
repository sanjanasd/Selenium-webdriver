import test_login
from test_login import test_login_automation

def test_logout_automation():
    test_login_automation()

    logout_button = test_login_automation.driver.find_element_by_xpath("/html/body/div[3]/form/input")
    logout_button.click()

if __name__=="__main__":
    test_logout_automation()    
    if len(test_login_automation.driver.find_elements_by_xpath("/html/body/div[3]/form/div[1]/input")):
        print("Pass")
    else: 
        print("Fail")

