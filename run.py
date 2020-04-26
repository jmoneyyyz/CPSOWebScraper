from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





from time import sleep



try:
	options = Options()
	options.headless = True
	options.add_argument("window-size=800,1200")  


	driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

	driver.get("https://doctors.cpso.on.ca/?search=general")
	element = driver.find_element_by_xpath("//label[@for='p_lt_ctl01_pageplaceholder_p_lt_ctl02_CPSO_AllDoctorsSearch_chkInactiveDoctors']")
	element.click()

	element = driver.find_element_by_id("p_lt_ctl01_pageplaceholder_p_lt_ctl02_CPSO_AllDoctorsSearch_btnSubmit1")
	element.click()


	# Get all doctor names (this works!)
	for i in range(5):
		currentPageNum = i+1
		nextPageNum = i+2
		#print(currentPageNum)


		# Get all data on the current page
		elements = driver.find_elements_by_class_name("doctor-search-results--result")
		for element in elements:
			doctorName = element.find_element_by_xpath(".//h3").text
			#print(doctorName + " - ", end="", flush=True)

			# Get Areas of Specialization
			specialty = ''
			specialtyElement = element.find_elements_by_xpath(".//*[contains(text(), 'Area(s) of Specialization:')]/following-sibling::p")
			if len(specialtyElement) > 0:
				specialty = specialtyElement[0].text

			# Get Location of Practice:
			location = ''
			locationElement = element.find_elements_by_xpath(".//*[contains(text(), 'Location of Practice:')]/following-sibling::p")
			if len(locationElement) > 0:
				location = locationElement[0].text

			# Get Fax Number
			faxNumber = '';
			locationElement = element.find_elements_by_xpath(".//*[contains(text(), 'Location of Practice:')]/following-sibling::p")
			if len(locationElement) > 0:
				location = locationElement[0].text
				if 'Fax:' in location:
					faxNumber = location[location.index('Fax:')+5:];

			print("\"" + doctorName.strip() + "\"" , ",", "\"" + faxNumber.strip() + "\"", ",", "\"" + specialty.strip() + "\"")

		# Go to the next page
		if currentPageNum%5 == 0:
			element = driver.find_element_by_link_text("Next 5")
		else:
			element = driver.find_element_by_link_text(str(nextPageNum))
		element.click()




except Exception as ex:
	print(ex)

sleep(7)
driver.quit()
