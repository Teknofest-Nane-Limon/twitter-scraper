from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from decouple import config
import pandas as pd


def make_search(search_key):
    driver.get(f"https://twitter.com/search?q={search_key}&src=typed_query")
    time.sleep(2)


def get_capture_tweets(scroll_page_size):
    for scroll in range(scroll_page_size):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        tweets = driver.find_elements(by=By.XPATH, value='//div[@data-testid="tweetText"]')
        times = driver.find_elements(by=By.XPATH, value='//time')
        time.sleep(2)
        [captured_tweets_time.add(t.get_attribute("datetime")) for t in times]
        [captured_tweets.add(tw.text) for tw in tweets]


def proc(keyword):
    make_search(keyword)
    time.sleep(2)
    get_capture_tweets(3)


def txt_read(path):
    with open(path, 'r', encoding='UTF-8') as file:
        while line := file.readline().rstrip():
            lines.append(line)


if __name__ == '__main__':
    df = pd.DataFrame()
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

    captured_tweets, captured_tweets_time = set(), set()
    lines = list()

    # keyword_list.txt aranmak istenen anahtar kelimelerin listesi
    txt_read('keyword_list.txt')

    for i in lines:
        try:
            proc(i)
        except Exception as ex:
            print(f'Hata oldu : " {i} " kelimesinde!\n {ex}')

    # [print(f"\n---- {i + 1}. Tweet ----\n{list(captured_tweets)[i]} Date: {list(captured_tweets_time)[i]}", "\n")
    # for i in range(len(captured_tweets))]

    df['Tweet'] = list(captured_tweets)

    # print(df.head(10))
    # print(df.info)
    df.to_csv('data.csv')
