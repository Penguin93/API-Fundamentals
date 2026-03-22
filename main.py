from weatherfetch import *
def login():
    while True:
        print("\nLogin to Weather API")
        print("1. Enter API key")
        print("2. I don't have an API key")
        print("3. Skip")
        option = input("Choose an option: ")

        if option == "1":
            api_key = input("Enter API key: ")
            break
        elif option == "2":
            print("Sign up at https://www.weatherapi.com/ to receive an API key")
        elif option == "3":
            break
        else:
            print("Invalid choice. Please try again.")
          

def main():
    while True:
        print("\nWeather Program")
        print("1. Search for Weather Data")
        print("2. View Weather Data")
        print("3. Remove Weather Data")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            city_name = input("Enter city name: ")
            print(f"fetch_weather(city_name)") #Replace with function later
        elif choice == "2":
            weather_data = input('View Weather Data')
            print(f"display_weather_info(weather_data)")#Replace with function later
        elif choice == "3":
            city_name = input("Enter  name to remove: ")
            print(f'Remove {city_name} from data list') #Replace with function later
        elif choice == "4":
            print("Exiting System.")
            break
        else:
            print("Invalid choice. Please try again.")

login()
if __name__ == "__main__":
    main()