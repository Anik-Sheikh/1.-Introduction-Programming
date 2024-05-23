def display_menu():                   
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("Display help:                          wildlife> help")
    print("Display help:                          wildlife> species Cairns") 
    print("Exit the application:                  wildlife> exit") 
  
def main():
    display_menu()  
    while True:
        user_input = input("wildlife> ").strip().lower() 
        if user_input == "help":
            display_menu()
        elif user_input == "exit":
            print("Exit")
            return  
        elif user_input.startswith('species'):
            temp = user_input.split(" ")
            city = temp[0]
            if len(temp) > 1:
                species_list = search_species(city)
                display_species(species_list)
            else:
                print("Errorr!")
        else:
            print("Error") 
            
def search_species(city):        
    species_list = [
        {"Species": {"TaxonID": 1039, "AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"TaxonID": 236, "AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]
    return species_list

def display_species(species_list):
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        taxon_id = species["Species"]["TaxonID"]
        print(f"TaxonID: {taxon_id}")
        print(f"AcceptedCommonName: {name}")
        print(f"Pest Status: {status}")
    
main()