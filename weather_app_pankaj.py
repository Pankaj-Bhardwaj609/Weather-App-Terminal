#Terminal Version of Weather Forecast App by Pankaj
import os
import requests
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')  #Get your API key from the weatherapi.com and set it in .env file

while True:
    city = input("\nEnter city name: ")

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\n--------Weather Forecast for {city}--------")
        print(f"\nCity: {data['location']['name']}")
        print(f"State: {data['location']['region']}")
        print(f"Country: {data['location']['country']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Weather: {data['current']['condition']['text']}")
        print(f"Local Time: {data['location']['localtime']}")
        print(f"Last Updated: {data['current']['last_updated']}")
    else:
        print("Invalid city name or API error")
    
    restart = input("Do you want to check weather for another city? ('y' for yes, 'n' for no): ").strip().lower()
    if restart != 'y':
        print("Exiting.... Goodbye!")
        break
