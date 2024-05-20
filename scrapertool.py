from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests

def MyDriver(folder, url):
    driver = webdriver.Chrome()
    driver.get(url)
    # Get the page source and parse it
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Create a directory to save the images
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Find all of the <img> tags on the page
    images = soup.findAll('img')
    
    #headers to avoid 403 forbidden error
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
    # Download each image
    for i, image in enumerate(images):
        # Use the 'src' attribute as the image url
        url = image['src']
        response = requests.get(url, headers=headers)
                
        try:
            with open(f'{folder}/' + url.split("/")[-1], 'wb') as file:
                file.write(response.content)
        except OSError as e:
            print(f"Warning: {e}")

            
            # Continue with other tasks or recovery steps
        # Open a file in write mode (binary) and write the image data to it
        # url_name = url.split("/")[-1]
        # url_name = ''.join(letter for letter in url_name if letter.isalnum())
        # url_name = url_name.replace(("=" and "?"), "") if ("=" or "?") in url_name else url_name
        # url_name = url_name + '.jpg' if '.jpg' not in url_name else url_name
        # with open(f'{folder}/' + url_name, 'wb') as file:
        #     file.write(response.content)

    driver.quit()

# for i in range(1,11):
#     url  = "https://www.myntra.com/full-sleeves?rawQuery=full%20sleeves" if (i == 1) else f"https://www.myntra.com/full-sleeves?p={i}&rawQuery=full%20sleeves"
#     folder = f'dataset/full-sleeves'
#     MyDriver(folder, url)

# for i in range(1,11):
#     url  = "https://www.myntra.com/half-sleeves?&rawQuery=half%20sleeves" if (i == 1) else f"https://www.myntra.com/half-sleeves?p={i}&rawQuery=half%20sleeves"
#     folder = f'dataset/half-sleeves'
#     MyDriver(folder, url)

# for i in range(1,11):
#     url  = "https://www.myntra.com/men-tshirts" if (i == 1) else f"https://www.myntra.com/men-tshirts?p={i}"
#     folder = 'genderdataset/Men'
#     MyDriver(folder, url)

for i in range(1,11):
    url  = "https://www.myntra.com/tops" if (i == 1) else f"https://www.myntra.com/tops?p={i}"
    folder = 'genderdataset/Women'
    MyDriver(folder, url)