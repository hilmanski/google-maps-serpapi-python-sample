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
    {
        "name": "The Corner House",
        "address": "102 18th Ave E, Seattle, WA 98112-5216"
    },
    {
        "name": "Green Lake Park",
        "address": "7201 E Green Lake Dr N, Seattle, WA 98115-5301"
    },
    {
        "name": "Demitri's Gourmet Mixes",
        "address": "8230 5th Ave S, Seattle, WA 98108-4533"
    }
]

# Helper function
def get_value(dictionary, key, default='Not available'):
    return dictionary.get(key, default)

# Query structure for Google Maps API
## q = Name + first two sections of address (street number and street name)

for source in sources:
    query = source['name'] + " " + source['address'].split(",")[0] + " " + source['address'].split(",")[1]
    
    result = client.search(
    	q=query,
    	engine="google_maps",
    )

    # Check if no place_results 
    if 'place_results' not in result:
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

