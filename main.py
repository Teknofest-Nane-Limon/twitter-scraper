from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from decouple import config


def make_search(search_key):
    search_input = driver.find_element(by=By.XPATH, value='//input[@data-testid="SearchBox_Search_Input"]')
    search_input.send_keys(search_key)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)


def get_capture_tweets(scroll_page_size):
    for scroll in range(scroll_page_size):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        tweets = driver.find_elements(by=By.XPATH, value='//div[@data-testid="tweetText"]')
        times = driver.find_elements(by=By.XPATH, value='//time')
        # print(f"***** {scroll}. Scroll *****")
        # [print(f"\n---------- {index}. Tweet ----------\n{i.text}", "\n") for index, i in enumerate(tweets)]
        # [print(f"\n---------- {index}. Times ----------\n{i.text}", "\n") for index, i in enumerate(times)]

        time.sleep(2)
        [captured_tweets.add(i.text) for i in tweets]
        [captured_tweets_time.add(i.get_attribute("datetime")) for i in times]
        time.sleep(2)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(2)

    username = driver.find_element(by=By.XPATH, value='//input')
    username.send_keys(config('EMAIL'))

    all_buttons = driver.find_elements(by=By.XPATH, value="//div[@role='button']")
    all_buttons[-2].click()

    time.sleep(2)

    password = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password.send_keys(config('PASSWORD'))
    driver.find_element(by=By.XPATH, value='//div[@data-testid="LoginForm_Login_Button"]').click()

    time.sleep(2)

    make_search("haklısınız")

    time.sleep(2)

    captured_tweets, captured_tweets_time = set(), set()

    get_capture_tweets(3)
    [print(f"\n---- {i+1}. Tweet ----\n{list(captured_tweets)[i]} Date: {list(captured_tweets_time)[i]}", "\n")
     for i in range(len(captured_tweets))]
