from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://codeforces.com/contests")
time.sleep(1)
contest = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[1]/div/div[4]/div[1]/a[1]")
x = contest.text
reg = input("the available contest is : "+x+" would you like to participate ? (y/n) : ")
if reg == 'y':
    element = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[1]/div/div[4]/div[1]/a[2]")
    element.click()
    usr = input("please enter your user name or email id : ")
    psd = input("please enter your password : ")
    element = driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
    element.send_keys(usr)
    element = driver.find_element_by_xpath('//*[@id="password"]')
    element.send_keys(psd)
    time.sleep(1)
    element = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input')
    element.click()
    time.sleep(1)
    element = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[3]/td/div/input')
    element.click()
    time.sleep(2)
    print("="*80)
    print("you have been successfully registered for the '"+x+"'contest")
    print("="*80)
    driver.close()
    driver.quit()
elif reg=='n':
    print("=" * 80)
    print("registration failed")
    print("=" * 80)
    driver.close()
    driver.quit()