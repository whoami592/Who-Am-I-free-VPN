import time

# VPN Name
VPN_NAME = "MR WHO AM I"

# List of countries (you can add more)
countries = {
    "1": "United States",
    "2": "United Kingdom",
    "3": "Canada",
    "4": "Australia",
    "5": "Japan"
}

def display_countries():
    print("\nAvailable countries:")
    for key, value in countries.items():
        print(f"{key}: {value}")

def connect_vpn(country):
    print(f"\nConnecting to {VPN_NAME}...")
    print(f"Selected country: {country}")
    time.sleep(2)  # Simulate connection delay
    print("Connection established successfully!")
    print(f"You are now connected to {country} via {VPN_NAME}.")

def main():
    print(f"Welcome to {VPN_NAME} VPN Setup")
    while True:
        display_countries()
        choice = input("\nSelect a country by number (or 'q' to quit): ").strip()
        
        if choice.lower() == 'q':
            print("Exiting VPN setup. Goodbye!")
            break
        elif choice in countries:
            connect_vpn(countries[choice])
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()