# About
Sample Google Maps API from SerpApi integration in Python. 

## Case
Input: list of names + address   
Output: Place details

## How
Install packages
```
pip install serpapi
pip install python-dotenv
```

API key setup
- create new .env file
- Add this line
```
SERPAPI_KEY=YOUR_API_KEY
```
- Replace `YOUR_API_KEY` with your real API key from SerpApi.

Run project
- locate your directory in terminal
- Run `python main.py`

## Notes
For bigger list, it's better to use a "thread/parallelization" method for faster result.