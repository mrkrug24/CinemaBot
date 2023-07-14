import time
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from find_flag import flag_dict

def get_list_movie_online(request_movie):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  
   
    # browser = webdriver.Chrome(executable_path = '/home/GreatCinema_bot/chromedriver', chrome_options = chrome_options, desired_capabilities = caps)
    browser = webdriver.Chrome('chromedriver', chrome_options = chrome_options, desired_capabilities = caps)
    
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    
    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    
    browser.get("https://ww2.lordsfilm.win/") 
    time.sleep(2)
    
    search_string = browser.find_element(by = By.CSS_SELECTOR, value = "#ajax_search") 
    search_string.send_keys(request_movie)  
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "#quicksearch > div > button > span") 
    search_button.click() 
    
    # time.sleep(2)
    
    dict_movie_link = {}
    
    request_movie = request_movie.lower()
    request_movie = request_movie.replace('-', ' ')
    request_movie = request_movie.replace(':', '')
    request_movie = request_movie.replace('!', '')
    request_movie = request_movie.replace('?', '')
    request_movie = request_movie.replace('.', '')
    request_movie = request_movie.replace(',', '')
    request_movie = request_movie.split(sep = ' ')
    
    # поиск нужного из списка
    time.sleep(1)
    # block_movies = browser.find_element(by = By.ID, value = 'dle-content')
    list_movies = browser.find_elements(by = By.CLASS_NAME, value = 'th-item')
    
    for movie in list_movies:
        name_of_movie = movie.find_element(by = By.CLASS_NAME, value = 'th-title')
        iter_name = name_of_movie.text
        iter_name = iter_name.lower()
        
        ans = 0
        
        for word in request_movie:
            if word in iter_name:
                ans = 1
                break
            
        if ans == 1:
            # iter_year = movie.find_element(by = By.CLASS_NAME, value = 'th-series')
            # iter_name = name_of_movie.text + ' (' + iter_year.text + ')'
            iter_name = name_of_movie.text
            
            button_watch = movie.find_element(by = By.TAG_NAME, value = "a")
            link_watch =  str(button_watch.get_attribute('href'))
            
            dict_movie_link[iter_name] = link_watch
            
    cnt_page = 0
    
    while True:
        try:
            navigation = browser.find_element(by = By.CLASS_NAME, value = 'navigation')
            button_navigation = navigation.find_elements(by = By.TAG_NAME, value = 'a')
            button_navigation[cnt_page].click()
            cnt_page += 1
            
            block_movies = browser.find_element(by = By.ID, value = 'dle-content')
            list_movies = block_movies.find_elements(by = By.CLASS_NAME, value = 'th-item')
            
            for movie in list_movies:
                name_of_movie = movie.find_element(by = By.CLASS_NAME, value = 'th-title')
                iter_name = name_of_movie.text
                iter_name = iter_name.lower()
                
                ans = 0
                
                for word in request_movie:
                    if word in iter_name:
                        ans = 1
                        break
                    
                if ans == 1:
                    iter_year = movie.find_element(by = By.CLASS_NAME, value = 'th-series')
                    iter_name = name_of_movie.text + ' (' + iter_year.text + ')'
                    
                    button_watch = movie.find_element(by = By.TAG_NAME, value = "a")
                    link_watch =  str(button_watch.get_attribute('href'))
                    
                    dict_movie_link[iter_name] = link_watch
        except:
            break
        
    return dict_movie_link
        
    
def get_movie_online(page_movie):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  
   
    # browser = webdriver.Chrome(executable_path = '/home/GreatCinema_bot/chromedriver', chrome_options = chrome_options, desired_capabilities = caps)
    browser = webdriver.Chrome('chromedriver', chrome_options = chrome_options, desired_capabilities = caps)
    
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    
    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    
    browser.get(page_movie)
    time.sleep(2)
    
    video_box = browser.find_element(by = By.CSS_SELECTOR, value = '#dle-content > article > div.fmain > div.fplayer.tabs-box > div:nth-child(3) > iframe')
    url_video = str(video_box.get_attribute('src'))                 
    
    block_image = browser.find_element(by = By.CSS_SELECTOR, value = '#dle-content > article > div.fmain > div.fcols.fx-row > div.fleft.fx-1.fx-row > div.fleft-img.fx-first > div > div.fposter.img-wide > img')
    url_image = str(block_image.get_attribute('src'))
    
    # block_info  
    block_year = browser.find_element(by = By.CSS_SELECTOR, value = '#dle-content > article > div.fmain > div.fcols.fx-row > div.fleft.fx-1.fx-row > div.fleft-desc.fx-1 > div.flists.fx-row > ul:nth-child(1) > li:nth-child(2) > span:nth-child(2)')
    year = '🎬 Год выхода: ' + block_year.text
    
    list_country = browser.find_element(by = By.CSS_SELECTOR, value = '#dle-content > article > div.fmain > div.fcols.fx-row > div.fleft.fx-1.fx-row > div.fleft-desc.fx-1 > div.flists.fx-row > ul:nth-child(1) > li:nth-child(2) > span:nth-child(3)')
    list_country = list_country.text
    list_country = list_country.replace(',', '')
    list_country = list_country.split(sep = ' ')
    
    res = '1'
    for i in list_country:
        if i == 'США':
            res = 'США'
            break
    
    if res != 'США':
        res = list_country[1]
    
    flag = flag_dict[res]
    country = flag + ' Страна: ' + res
    
    info_movie = year + '\n' + country
    
    block_imdb = browser.find_element(by = By.CSS_SELECTOR, value = '#dle-content > article > div.fmain > div.fcols.fx-row > div.fleft.fx-1.fx-row > div.fleft-desc.fx-1 > div.flists.fx-row > ul:nth-child(4) > li > div.frate.frate-imdb > span')
  
    if block_imdb.text != '':
        good = float(block_imdb.text)
    
        if good >= 8:
            imdb = '💚 Рейтинг: IMDB ' + block_imdb.text
        elif good >= 6:
            imdb = '💛 Рейтинг: IMDB ' + block_imdb.text
        else:
            imdb = '❤️ Рейтинг: IMDB ' + block_imdb.text
            
        info_movie += '\n' + imdb + '0'
    
    about_movie = []
    about_movie.append(url_image)
    about_movie.append(url_video)
    about_movie.append(info_movie)
    
    return about_movie