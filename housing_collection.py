import requests, time, pandas
from bs4 import BeautifulSoup
from datetime import date

today = date.today()

# Empty lists to be populated with desired data
home_price = []
home_address = []
home_rooms = []
home_baths = []
home_sq_foot = []
home_link = []

## Script bellow scrapes home data based on desired criteria. Tried other websites but Homes.com was the easiest one to work with and my search query was saved when coppied and pasted to a new tab/browser. ##
try:
    ### WEB SCRAPING 
    # Repalce url with url that you specify. Filter parameters such as min/max price are saved to search URL.
    homes_p1 = "https://www.homes.com/houses-for-sale/p1/?search parameters you specify via website's filters such as price, rooms, etc."
    header = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Accept-Language" : "en-US,en;q=0.9",
    }

    response = requests.get(url=homes_p1, 
                            headers=header)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")

    # Get total pages
    try:
        page_range = int(soup.find(class_="pageRange").text[-1]) # If query is only one page long, code will generate an error without try/except.
        print(f"page range: {page_range}")
    
    except AttributeError:
        page_range = 1

    print("Looping through pages...")
    time.sleep(3)
    
    for page in range(page_range):
        query_site = f"https://www.homes.com/houses-for-sale/p{page + 1}/?search parameters you specify via website's filters such as price, rooms, etc."
        print(f"Page: {query_site}")
        response = requests.get(url=query_site, 
                            headers=header)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        home_card = soup.find_all("li", class_="placard-container")
        
        # For loop to populate lists from soup data
        for element in home_card:
            price_list = element.find(class_="price-container").text.split()
            home_price.append(price_list[0]) # Populate home_price
            home_address.append(element.find(class_="property-name").text) # Populate home_address
            home_info = element.find(class_="detailed-info-container").text.split('\n')
            home_rooms.append(home_info[1]) # Populate home_rooms
            home_baths.append(home_info[2]) # Populate home_baths
            home_sq_foot.append(home_info[3]) # Populate home_sq_foot
            property_container = element.find("a").get("href")
            home_link.append("https://www.homes.com/" + property_container) # Populate home_link
        print(f"SUCCESS: Page {page + 1} data gathered.")
        time.sleep(3)
    print("All data gathered...creating csv.")

    ### CSV CREATION
    home_dict = {"Price" : home_price,
                "Home Address" : home_address,
                "Rooms" : home_rooms,
                "Bathrooms" : home_baths,
                "Square Footage" : home_sq_foot,
                "Link to Home" : home_link,
                "Date" : date.today()}
    home_data = pandas.DataFrame(home_dict)
    home_data.to_csv(f"./Daily_Export/{today}_homes_export.csv")
    print("SUCCESS: CSV created and saved in 'Daily_Export' folder!")

except:
    home_dict = {"Price" : home_price,
            "Home Address" : home_address,
            "Rooms" : home_rooms,
            "Bathrooms" : home_baths,
            "Square Footage" : home_sq_foot,
            "Link to Home" : home_link,
            "Date" : date.today()}
    home_data = pandas.DataFrame(home_dict)
    home_data.to_csv(f"./Daily_Export/ERROR-{today}_homes_export.csv")
    print("FAILURE: CSV created and saved in 'Daily_Export' folder. NO DATA IN FILE.")