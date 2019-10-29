from selenium import webdriver
from openpyxl import Workbook
from time import sleep
import re

from credentials import username, password

driver = webdriver.Chrome('./chromedriver')  # opens new chrome window
driver.get('https://ntu-signon-sg.inplacesoftware.com')
driver.find_element_by_link_text('Staff and Students').click()

username_input = driver.find_element_by_name('j_username')
password_input = driver.find_element_by_name('j_password')
username_input.send_keys(username)
password_input.send_keys(password)
driver.find_element_by_id('login').submit()

sleep(3)  # wait for 3 second for page to load

data = []
url = 'https://ntu-stu-sg.inplacesoftware.com/opportunity/'

for opportunity_number in range(269, 400):
    opportunity_url = url+str(opportunity_number)
    driver.get(opportunity_url)

    sleep(0.5)  # wait for 0.5 second for page to load
    main_content = driver.find_elements_by_tag_name('article')
    sleep(0.5)  # wait for 0.5 second for main_content to be processed

    if (main_content):
        role = driver.find_element_by_css_selector('h1.ng-binding').text
        employer = main_content[0].text.strip('Employer\n')
        description = main_content[1].text.strip('Description\n')
        allowance = ''
        application_instructions = ''
        application_requirements = ''
        email = ''

        for article in main_content:
            if (article.text.startswith('Allowance')):
                allowance = article.text.strip(
                    'Allowance (CPF excempted)\n')

            if (article.text.startswith('Application Instructions')):
                application_instructions = article.text.strip(
                    'Application Instructions\n')

            if (article.text.startswith('Application Requirements')):
                application_requirements = article.text.strip(
                    'Application Requirements\n')

        try:
            email = re.findall(
                '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+)', application_instruction)[0]
        except:
            pass

        data.append([role, employer, description, allowance, application_instructions,
                        application_requirements, email, opportunity_url])

    # wait for data to get processed
    sleep(0.5)

# save data to excel sheet
workbook = Workbook()
worksheet = workbook.active
worksheet.append(['Role', 'Employer', 'Description', 'Allowance',
                    'Instructions', 'Requirements', 'Email', 'URL'])

for each_data in data:
    worksheet.append(each_data)

workbook.save(filename='Internship.xlsx')
