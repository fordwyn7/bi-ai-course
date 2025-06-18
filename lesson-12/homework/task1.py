from bs4 import BeautifulSoup


with open("weather.html", "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Print the headers of the table
    for th in soup.find_all("th"):
        print(th.text, end=" ")
        
    # Print the data in the table
    for tr in soup.find_all("tr"):
        for td in tr.find_all("td"):
            print(td.text, end=" ")
        print()
        
    temp = {}
    for day in range(0, len(soup.find_all("td")) - 1, 3):
        tds = soup.find_all("td")
        temp[tds[day].text] = [tds[day + 1].text[:-2], tds[day + 2].text]
        
    mx_temp = 0  # Variable to store the maximum temperature
    day = ""
    for key, value in temp.items():
        if int(value[0]) > mx_temp:
            mx_temp = int(value[0])
            day = key
    print(f"\n\nThe maximum temperature is {mx_temp} on {day}.")
    
    # Sunny days 
    sunny_days = []
    for key, value in temp.items():
        if value[1] == "Sunny":
            sunny_days.append(key)
    print(f"\nSunny days: {', '.join(sunny_days)}")    
