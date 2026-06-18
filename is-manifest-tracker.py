import requests

url = "http://open-notify.org"

print("📡 Connecting to Earth's orbit servers...")

try:
    # 1. Knock on the network door
    response = requests.get(url, timeout=10)
    
    # 2. Check if the server responded with success code 200
    if response.status_code == 200:
        data = response.json()
        
        # Pull out the massive list of astronaut data blocks
        astronaut_list = data["people"]
        
        print(f"\n🚀 SUCCESS! There are {data['number']} humans outside Earth.")
        print("📋 Printing the official manifest of space travelers:\n")
        
        # 🔄 The Loop Engine
        count = 1
        for astro in astronaut_list:
            name = astro["name"]
            craft = astro["craft"]
            print(f"{count}. 👨‍🚀 {name} | Living on: 🛰️ {craft}")
            count = count + 1
            
        print("\n🏁 Manifest download complete. Loop terminated successfully.")
    else:
        print(f"⚠️ Server hitch. Error code: {response.status_code}")

except ValueError:
    # This catches the JSON crash error you just saw!
    print("🛑 API Error: The NASA server sent back broken data. It is temporarily overloaded.")

except requests.exceptions.RequestException:
    # This catches internet disconnects
    print("❌ Network Error: Could not connect to the internet!")
