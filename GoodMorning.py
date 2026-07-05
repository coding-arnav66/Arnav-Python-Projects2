import requests, os
from bs4 import BeautifulSoup
import randfacts
import pyjokes

name = input("Enter your first name: ").strip()
print(f"🌞 Good morning {name if name else 'Friend'}!\n\n")
print(""" Menu:
1. Weather
2. Headlines
3. Fact of the Day
4. Joke of the Day
5. Routine Generator""")
def weather():
    url = "https://weather-forecast.com"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find('div', class_="small-12 medium-6 columns list-side-cont flag-sprites")

        if container:

            lines = [line.strip() for line in container.text.split("\n") if line.strip()]
            print("\n🌍 Today's Weather Report:\n")
            for line in lines:
                # Format city and temperature nicely
                if "-" in line:
                    parts = [p.strip() for p in line.split("-") if p.strip()]
                    if len(parts) == 2:
                        city, temp = parts
                        print(f"• {city}: {temp}°C")
                    else:
                        print(f"• {line}")
                else:
                    print(f"• {line}")
        else:
            print("No weather data found on the page.")
    except Exception as e:
        print("Weather data could not be fetched:", e)



def headlines():
    url = "https://timesofindia.indiatimes.com/"
    try:
        response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('div', class_="Kt6Pm style_change T5Q6J")
        no = 0
        for headline in headlines:
            print(headline.text.strip(), "\n")
            no += 1
            if no == 10:
                break


    except Exception as d:
        print(d)

def facts():
    fact = randfacts.get_fact()
    print(f"\n\nTodays fact:\n{fact}\n\n")

def joke():
    joke = pyjokes.get_joke()
    print(f"Todays joke:\n{joke}\n\n")
def routine():
    user = input("You want to get your routine?(yes/no): ")
    if "yes" in user.lower():
        print("Time for your routine!")
        to_do = input("Type the things you want to have in your routine seperated by commas only: ")
        to_do_list = list(to_do.split(","))
        print(f"\nThis is your ready-to-go prompt. Paste it on any AI chatbox to get your routine:\n\nCreate a comprehensive, efficient, and realistic daily schedule based on the following list of tasks and goals. Organize these items logically throughout the day, ensuring a good balance between work, breaks, and personal time. The tasks to be included are: {to_do_list}. Please provide a well-structured hourly or time-blocked routine.")

    else:
        print("Skipped personalised routine...")

mast = input("Press enter to continue: ")
weather()
mast = input("Press enter to continue: ")
headlines()
mast = input("Press enter to continue: ")
facts()
mast = input("Press enter to continue: ")
joke()
mast = input("Press enter to continue: ")
routine()
print("Have a great day!🌟")






