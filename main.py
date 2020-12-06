import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    number_of_votes = 10
    num_of_questions = 4
    for i in range(0, number_of_votes):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.get("https://ru.surveymonkey.com/r/MT5KVPB")
        print("loaded")
        survey = driver.find_element_by_name("surveyForm")
        random.seed(9675)
        for i in range(num_of_questions):
            question_row = survey.find_elements_by_xpath(".//*")[0].find_elements_by_xpath("./div")[i]
            question_field = question_row.find_elements_by_css_selector("*")[0].find_elements_by_css_selector("*")[0]
            name = question_field.get_attribute("data-question-id")
            elements = question_field.find_elements_by_name(name)
            randPos = random.randrange(0, len(elements), 1)
            selected = elements[randPos]
            driver.execute_script("arguments[0].click()", selected)
        survey.submit()
        driver.close()
