def display_menu():                 
    print("Help")
    print("====")
    print("The following commands are recognized:")
    print("Display help:                          wildlife> help")
    print("Display help:                          wildlife> species Cairns") 
    print("Display help:                          wildlife> sightings Cairns 1039")
    print("Display help:                          wildlife> species Cairns venomous")
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
            city = temp[1]
            if len(temp) > 2 and temp[2] == 'venomous':
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                species_list = search_species(city)
                display_species(species_list)
                coordinates = gps(city)
                print(f"Coordinates for {city}: Latitude: {coordinates['latitude']}, Longitude: {coordinates['longitude']}")
        elif user_input.startswith('sightings'):
            _, city, taxon_id = user_input.split(maxsplit=2)
            sightings = search_sightings(city, taxon_id)
            display_sightings(sightings)
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
        
        
def search_sightings(taxonid, city):      
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_sightings(sightings):
    print("Animal sightings:")
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Start Date: {start_date}, Locality: {locality}")
        
        
def filter_venomous(species_list):         
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]


def gps(city):
    city_coordinates = {
        "Brisbane": {"latitude": -27.4689, "longitude": 153.0234},
    }
    return city_coordinates.get(city, {"latitude": -27.4689, "longitude": 153.0234})

    
main() 

