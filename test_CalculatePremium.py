import test_login
from test_login import test_login_automation
from selenium.webdriver.support.select import Select
import time

def test_calculatepremium_automation():
    
    test_login_automation() #call login method from test_login

    #Navigate to Request Quotation tab
    request_quotation =  test_login_automation.driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a")
    request_quotation.click()

    #Enter the text boxes to calculate premium
    INCIDENTS = input("Enter in your Incident:")
    REGISTRATION = input("Enter in your Registration Number:")
    ANNUALMILEAGE = input("Enter in your Annual Mileage:")
    ESTIMATEDVALUE = input("Enter in your current Estimated Value:")

    #Send all the entered values to the respective blocks
    incident_input = test_login_automation.driver.find_element_by_id("quotation_incidents")
    incident_input.send_keys(INCIDENTS)

    registration_input = test_login_automation.driver.find_element_by_id("quotation_vehicle_attributes_registration")
    registration_input.send_keys(REGISTRATION)

    annualmileage_input = test_login_automation.driver.find_element_by_id("quotation_vehicle_attributes_mileage")
    annualmileage_input.send_keys(ANNUALMILEAGE)

    estimatedvalue_input = test_login_automation.driver.find_element_by_id("quotation_vehicle_attributes_value")
    estimatedvalue_input.send_keys(ESTIMATEDVALUE)

    # Selecting different options from dropdown
    #Break down Dropdown
    breakdowncover =  Select(test_login_automation.driver.find_element_by_id("quotation_breakdowncover"))
    all_breakdowncover = breakdowncover.options

    #Parking Location Dropdown
    parkinglocation =  Select(test_login_automation.driver.find_element_by_id("quotation_vehicle_attributes_parkinglocation"))
    all_parkinglocation = parkinglocation.options

    #Wind shild replacement checking buttons
    Yes = test_login_automation.driver.find_element_by_id("quotation_windscreenrepair_t")
    No = test_login_automation.driver.find_element_by_id("quotation_windscreenrepair_f")

    #Calculate Premium Button
    calculatepremium =  test_login_automation.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/div[8]/input[1]")

    # Looping through each dropdown
    for i in ['Yes', 'No']:
        vars()[i].click()
        #i.click()
        for j in all_breakdowncover:
            j.click()
            for k in all_parkinglocation:
                k.click()
                calculatepremium.click()
                time.sleep(1)
                print("Incident =" , INCIDENTS)
                print("Registration number = ", REGISTRATION)
                print("Annual Mileage =",ANNUALMILEAGE)
                print("Current estimated Value =", ESTIMATEDVALUE)
                print("windshield Repair = ", i)
                print("breakdown =",j.text)
                print("Parking Location =", k.text)
                ele = test_login_automation.driver.find_element_by_id("calculatedpremium")
                print(ele.text)
                print("\n")

test_calculatepremium_automation()

