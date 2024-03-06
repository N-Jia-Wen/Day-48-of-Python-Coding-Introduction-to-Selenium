from selenium import webdriver
from selenium.webdriver.common.by import By

# These options keep Chrome browser open after program finishes:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

time_list = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last time")
time_list = [date.text for date in time_list]

name_list = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last li a")
name_list = [event_name.text for event_name in name_list]

event_dictionary = {num: {"time": time_list[num], "name": name_list[num]} for num in range(0, len(time_list))}
print(event_dictionary)


driver.quit()
