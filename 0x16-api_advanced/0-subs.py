#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        # Send the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid or other status codes
            return 0
    except Exception as e:
        # Return 0 in case of any exceptions
        return 0
