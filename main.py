import os
import serpapi

from dotenv import load_dotenv
load_dotenv()

client = serpapi.Client(api_key=os.getenv('SERPAPI_KEY'))


# Input/Given
## You might want to import this dynamically from a file/database
sources = [
    {
        "name": "Sea Monster",
        "address": "2202 N 45th St, Seattle, WA 98103-6904"
    },
    {
        "name": "NEXUS",
        "address": "1808 Minor Ave, Seattle, WA 98101-1414"
    },
    {"name": "Sur La Table", "address": "6100 4th Ave S, Seattle, WA 98108-3215"},
    {"name": "Snoqualmie P-Patch Community Gardens", "address": "4549 13th Ave S, Seattle, WA 98108-1808"},
    {"name": "Arrive Belay & Noba", "address": "6559 15th Ave NW, Seattle, WA 98117-5506"},
    {"name": "Poke Cafe", "address": "334 NE Northgate Way, Seattle, WA 98125"},
    {"name": "QFC", "address": "1401 Broadway Ct, Seattle, WA 98122"} 
]

# Helper function
def get_value(dictionary, key, default='Not available'):
    return dictionary.get(key, default)

# Query structure for Google Maps API
## q = Name + first two sections of address (street number and street name)

for source in sources:
    query = source['name'] + ", " + source['address'].split(",")[1] + ", " + source['address'].split(",")[0] 
    
    result = client.search(
    	q=query,
    	engine="google_maps",
    )

    # Handling multiple results
    if 'local_results' in result:
        print(f"We found multiple results, fetching the first one")
        print(f"----------------------------------------------")
        result = client.search(
            engine="google_maps",
            place_id=result['local_results'][0]['place_id']
        )
        
    # Handling no results
    if 'local_results' not in result and 'place_results' not in result:
        print(f"Name: {source['name']} : Not Found in Google Maps")
        print(f"----------------------------------------------")
        continue
    
    place_result = result['place_results']
    # Feel free to adjust the output as needed
    ## Available Key reference: https://serpapi.com/playground?engine=google_maps&q=sea+monster+2202+N+45th+St%2C+Seattle&ll=%4040.7455096%2C-74.0083012%2C14z&hl=en&type=search
    print(f"Name: {get_value(place_result, 'title')}")
    print(f"Address: {get_value(place_result, 'address')}")
    print(f"Phone Number: {get_value(place_result, 'phone')}")
    print(f"Website: {get_value(place_result, 'website')}")
    print(f"----------------------------------------------")

