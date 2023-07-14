import time
from os import times_result
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from find_flag import flag_dict

def get_list_series_download(request_movie):
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
   
    # browser = webdriver.Chrome(chrome_options = chrome_options, desired_capabilities = caps)
    
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
    
    browser.get("https://mm.anwap.tube/serials/search") 
    
    search_string = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(1) > input[type=text]") 
    search_string.send_keys(request_movie)
     
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > label > input[type=checkbox]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(4) > input[type=submit]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > input[type=submit]") 
    search_button.click() 
    
    # time.sleep(1)
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
    block_movies = browser.find_element(by = By.CLASS_NAME, value = 'blm')
    list_movies = block_movies.find_elements_by_css_selector('.my_razdel.film')
    
    for movie in list_movies:
        name_of_movie = movie.find_element(by = By.CLASS_NAME, value = 'namefilm')
        iter_name = name_of_movie.text
        iter_name = iter_name.lower()
        
        ans = 0
        
        for word in request_movie:
            if word in iter_name:
                ans = 1
                break
            
        if ans == 1:
            iter_year = movie.find_element_by_css_selector('.in.year')
            iter_name = name_of_movie.text + ' (' + iter_year.text + ')'
            
            dict_movie_link[iter_name] = name_of_movie
            
    browser.quit()
            
    return dict_movie_link
        
    
    
def get_series_download(request_movie, full_name):
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
   
    browser = webdriver.Chrome(chrome_options = chrome_options, desired_capabilities = caps)
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
    
    browser.get("https://mm.anwap.tube/serials/search") 
    
    search_string = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(1) > input[type=text]") 
    search_string.send_keys(request_movie)
     
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > label > input[type=checkbox]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(4) > input[type=submit]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > input[type=submit]") 
    search_button.click() 
    
    
    # time.sleep(1)
    block_movies = browser.find_element(by = By.CLASS_NAME, value = 'blm')
    list_movies = block_movies.find_elements_by_css_selector('.my_razdel.film')
    
   
    
    for movie in list_movies:
        name_of_movie = movie.find_element(by = By.CLASS_NAME, value = 'namefilm')
        
        if name_of_movie.text == full_name:
            button_page = movie.find_element(by = By.CLASS_NAME, value = 'opisfilm')
            button_page.click()

            
            block_image = browser.find_element(by = By.CSS_SELECTOR, value = 'body > div.blm > div.filmopis.screen > img') 
            url_image = str(block_image.get_attribute('src'))              
            
            block_info = browser.find_element(by = By.TAG_NAME, value = 'tbody')
            list_movies = block_info.find_elements(By.TAG_NAME, value = 'tr')
            
            chk_imdb = 0
            
            for movie in list_movies:
                topic = movie.find_element(By.TAG_NAME, value = 'td')
                
                if topic.text == 'Год:':
                    year_info = movie.find_element(By.TAG_NAME, value = 'a')
                    year = '🎬 Год выхода: ' + year_info.text 
                    
                if topic.text == 'Страна:':
                    country_info = movie.find_elements(By.TAG_NAME, value = 'a')
                    res = '1'
                    if len(country_info) == 0:
                        topic_2 = movie.find_elements(By.TAG_NAME, value = 'td')
                        res = topic_2[1].text
                    else:
                        for i in country_info:
                            if i.text == 'США':
                                res = 'США'
                                break
                        if res != 'США':
                            res = country_info[0].text
                        
                    flag = flag_dict[res]
                    country = flag + ' Страна: ' + res 
                    
                if topic.text == 'Рейтинг:':
                    imdb_info = movie.find_elements(By.TAG_NAME, value = 'td')
                    imdb_pre = imdb_info[1].text
                    spl_string = imdb_pre.split('/')
                    res = spl_string[0]
                    
                    if len(res) > 1:
                        res += '0'
                    
                    good = float(res)
                    
                    if good >= 8:
                        imdb = '💚 Рейтинг: IMDB ' + res
                    elif good >= 6:
                        imdb = '💛 Рейтинг: IMDB ' + res
                    else:
                        imdb = '❤️ Рейтинг: IMDB ' + res

                    chk_imdb = 1
            
            
            if chk_imdb == 1:
                info_movie = year + '\n' + country + '\n' + imdb
            else:
                info_movie = year + '\n' + country
                
                
            list_series = {}
            block_series = browser.find_element(by = By.CLASS_NAME, value = 'tl2') 
            series = block_series.find_elements(by = By.TAG_NAME, value = 'a') 
            
            
            part_name = 'Сезон '
            cnt = 1
            for item in series:
                full_part = part_name + str(cnt)
                list_series[full_part] = item.get_attribute('href')
                cnt += 1
                
                
            about_movie = []
            about_movie.append(url_image)
            about_movie.append(list_series)
            about_movie.append(info_movie)
            
            break
    
    return about_movie 
    
    
def get_list_of_ser_download(request_series, full_name, number):
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
   
    browser = webdriver.Chrome(chrome_options = chrome_options, desired_capabilities = caps)
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
    

    browser.get("https://mm.anwap.tube/serials/search") 
    
    search_string = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(1) > input[type=text]") 
    search_string.send_keys(request_series)
     
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > label > input[type=checkbox]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(4) > input[type=submit]") 
    search_button.click() 
    
    search_button = browser.find_element(by = By.CSS_SELECTOR, value = "body > div.blm > form > div:nth-child(3) > input[type=submit]") 
    search_button.click() 
    
    block_movies = browser.find_element(by = By.CLASS_NAME, value = 'blm')
    list_movies = block_movies.find_elements_by_css_selector('.my_razdel.film')
    
    
    for movie in list_movies:
        name_of_movie = movie.find_element(by = By.CLASS_NAME, value = 'namefilm')
        
        if name_of_movie.text == full_name:
            button_page = movie.find_element(by = By.CLASS_NAME, value = 'opisfilm')
            button_page.click()
            break
        
    time.sleep(1)
    
    block_series = browser.find_element(by = By.CLASS_NAME, value = 'tl2') 
    series = block_series.find_elements(by = By.TAG_NAME, value = 'a') 
    series[number - 1].click() 
    
    time.sleep(1)
    
    block_ser = browser.find_elements(by = By.TAG_NAME, value = 'li')
    list_href = {}

    for ser in block_ser:
        iter = ser.find_element(by = By.TAG_NAME, value = 'a')
        list_href[iter.text] = iter.get_attribute('href')
    
    for ser in list_href:
        browser.get(list_href[ser]) 
        block_ser = browser.find_elements(by = By.CLASS_NAME, value = 'tlsiconkoi')
        dif = block_ser[1].find_elements(by = By.TAG_NAME, value = 'a')
        biggest = dif[-1].get_attribute('href')
        list_href[ser] = biggest
        
    return list_href