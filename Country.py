'''
Joshua Brock
CIS261
Country
'''

from sre_constants import CATEGORY_UNI_NOT_LINEBREAK


def display_menu():
    print("Command Menu")
    print("view --> View country name")
    print("add --> Add a country")
    print("delete --> Delete a country")
    print("exit --> Close the application")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country Codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country Name: {name}. /n")
    else:
        print("There is no Country with that code.")
        
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using that code")
    else:
        name = input("Enter Country Name :")
        name = name.title()
        countries[code] = name
        print(f"{name} was added /n")
        
def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted /n")
    else:
        print("There is no country with that code /n")
        
def main():
    countries = {"AF": "Afghanistan", "DE": "Germany", "US": "United States"}
    
    display_menu()
    
    while True:
        command = input("Enter a command :")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            print("Bye")
            break
        else:
            print("Invalid command, please try again")
            
if __name__ == '__main__':
    main()
    
    

        
