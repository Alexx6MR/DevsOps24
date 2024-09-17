# Använd requests.get för att hämta en lista över produkter från https://dummyjson.com/products.
# 	•	Filtrera produkterna för att bara visa de som har ett pris under 100.
# 	•	Skriv ut produktnamnet och priset för varje produkt som uppfyller kriterierna.

import requests
import json
import logging



def GetAllLowPriceProduct():
   
    try:
        data = requests.get("https://dummyjson.com/products?where=price<100&select=title,price&sortBy=price")
   
        if(data.status_code == 200):
            res = data.json()
            print(res)
        else:
            logging.error(f"Error: Not posible to fetch all products, code: {data.status_code} ")
    except:
        logging.error("Something went wrong trying to get All prodruct")
  




def main():
    GetAllLowPriceProduct()

if __name__ == "__main__":
    main()