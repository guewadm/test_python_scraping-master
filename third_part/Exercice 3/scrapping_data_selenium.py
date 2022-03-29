from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

data = {
    "names": [],
    "breadcrumb ": [],
}

# A list of two URL's

listurl = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

# Boucle dans la liste

for i in listurl:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(i)
    
    # Cliquez sur la fenêtre popup des cookies
    
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.LINK_TEXT,"Continuer sans accepter"))).click()

    # Obtenir les éléments
    
    try:
        
        zone = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.CLASS_NAME, "shop-notification"))
           )
        offres = zone.find_elements_by_css_selector("shop-content")
        for offre in offres:
            names = (offre.find_element_by_css_selector("#search-content > div > shared-grid > div > div:nth-child(1) > shared-product-tile > section > div.shelfProductTile-content > div.shelfProductTile-information > header")).text
            print(names)
            breadcrumb = (offre.find_element_by_css_selector("span")).text
            print(breadcrumb)
            
            data["names"].append(names)
            data["breadcrumb"].append(breadcrumb)
   
        except Exception as ex:
        print(ex)
    driver.quit()
df = pd.DataFrame.from_dict(data)
print('aaaaaaaaaaa')
print(len(data))
print(df)
df.to_csv("results.csv")




