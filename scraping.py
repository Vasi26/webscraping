import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
class Flipkart:
    def __init__(self):
        self.base_url = "https://www.flipkart.com"
        
    def intro(self):
        print("-----------------Welcome To Flipkart-----------------")
        print(">>>>>>Choose Category You want to Purchase<<<<<<<<")
        print("1. Mobiles & Electronics")
        print("2. Grocery Items")
        print("3. Clothing")
        category = input("Enter the number corresponding to the desired category:")
        
        try:
            category = int(category)
            
            if category == 1:
                try:
                    self.get_mobiles_electronics()
                except Exception as e:
                    print(f"An error occurred while fetching mobiles and electronics: {str(e)}")
            elif category == 2:
                try:
                    self.get_grocery()
                except Exception as e:
                    print(f"An error occurred while fetching grocery items: {str(e)}")
            elif category == 3:
                try:
                    self.get_clothing()
                except Exception as e:
                    print(f"An error occurred while fetching clothing items: {str(e)}")
            else:
                print("Invalid category number! Please enter a correct category number.")
                self.intro()
        except ValueError:
            print("Invalid input! Please enter a number corresponding to the desired category.")
            self.intro()
        
    def make_request(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def get_mobiles_electronics(self):
        try:
            product_name = input("Enter Product Name:").strip().lower()
            
            if product_name == 'samsung':
                product_name = 'samsung mobiles'
            
            url = f"{self.base_url}/search?q={product_name}"
            soup = self.make_request(url)
            
            links = soup.find_all("a", class_="_1fQZEK")
            
            data = [] # Create an empty dictionary to store the data
            
            for link in links:
                href = link.get('href')
                link_url = f"{self.base_url}{href}"
                response2 = requests.get(link_url)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                
                product_name = soup2.find("span", class_="B_NuCI").text
                price = soup2.find("div", class_="_30jeq3 _16Jk6d").text
                description = soup2.find("div", class_="_2418kt").text
                reviews = soup2.find_all('div', class_='t-ZTKy')
                Reviews= [Reviews.get_text() for Reviews in reviews]

                # Append the product information as a dictionary to the data list
                data.append({
                    'Title':product_name,
                    'Price':price,
                    'Terms_conditions':description,
                    'Reviews':Reviews

                })
                
            with open('products.csv','w',newline='',encoding='utf-8') as file:
                fields_names=['Title','Price','Terms_conditions','Reviews']
                dict=csv.DictWriter(file,fieldnames=fields_names)
                dict.writeheader()
                dict.writerows(data)
                 
            df=pd.read_csv('products.csv')
            data=pd.DataFrame(data)
            file=data.to_csv(r'D:/webscrap/mobiles_electronics.csv')  # Saving Extracted data in csv format
            print(df)                            
        except Exception as e:
            print(f"An error occurred while fetching mobiles and electronics: {str(e)}")
    def get_grocery(self):
        try:
            product_name = input("Enter Product Name:").strip().lower()
            url = f"{self.base_url}/search?q={product_name}"
            soup = self.make_request(url)
            
            links = soup.find_all('a', class_='_2rpwqI')
            
            data = [] # Create an empty list to store the data
            
            for link in links:
                href = link.get('href')
                link_url = f"{self.base_url}{href}"
                response2 = requests.get(link_url)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                
                product_details = soup2.find('span', class_='B_NuCI').text
                product_price = soup2.find('div', class_='_30jeq3 _16Jk6d').text
                product_specification = soup2.find('table', class_='_14cfVK').text
                rating = soup2.find('div', class_='_3LWZlK').text
                reviews = soup2.find_all('div', class_='t-ZTKy')
                
                # Append the product information as a dictionary to the data list
                data.append({
                    'Title': product_details,
                    'Rating': rating,
                    'Price': product_price,
                    'Specifications': product_specification,
                    'Reviews': [review.get_text() for review in reviews],
                })
            with open('products.csv','w',newline='',encoding='utf-8') as file:
                fields_names=['Title','Rating','Price','Specifications','Reviews']
                dict=csv.DictWriter(file,fieldnames=fields_names)
                dict.writeheader()
                dict.writerows(data)
                 
            df=pd.read_csv('products.csv')
            data=pd.DataFrame(data)
            file=data.to_csv(r'D:/webscrap/grocery.csv')  # Saving Extracted data in csv format
            print(df)             
        except Exception as e:
            print(f"An error occurred while fetching grocery items: {str(e)}")

    def get_clothing(self):
        try:
            product_name = input("Enter Product Name:").strip().lower()
            url = f"{self.base_url}/search?q={product_name}"
            soup = self.make_request(url)
            
            links = soup.find_all('a', class_='_2UzuFa')
            
            data = [] # Create an empty list to store the data
            
            for link in links:
                href = link.get('href')
                link_url = f"{self.base_url}{href}"
                response2 = requests.get(link_url)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                
                brand = soup2.find('span', class_='G6XhRU').text
                product_details = soup2.find('span', class_='B_NuCI').text
                price = soup2.find("div", class_='_30jeq3 _16Jk6d').text
                reviews1 = soup2.find_all('div', class_='_6K-7Co')
                
                # Append the product information as a dictionary to the data list
                data.append({
                    'Brand Name': brand,
                    'Product Name': product_details,
                    'Price': price,
                    'Reviews': [review.get_text() for review in reviews1],
                })
            
            with open('products.csv','w',newline='',encoding='utf-8') as file:
                fields_names=['Brand Name','Product Name','Price','Reviews']
                dict=csv.DictWriter(file,fieldnames=fields_names)
                dict.writeheader()
                dict.writerows(data)
                 
            df=pd.read_csv('products.csv')
            data=pd.DataFrame(data)
            file=data.to_csv(r'D:/webscrap/clothing.csv')   # Saving Extracted data in csv format
            print(df)
            
        except Exception as e:
            print(f"An error occurred while fetching clothing items: {str(e)}")

obj = Flipkart()
obj.intro()

