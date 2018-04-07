import requests

def run_query(search_term):

    # your bing api key here
    subscription_key = ''
    assert subscription_key

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    # The count parameter specifies the number of results to return in the response, max is 100
    params  = {"q": search_term, 'count' : 5, }

    response = requests.get(search_url, headers=headers, params=params)

    response.raise_for_status()
    search_results = response.json()

    descriptions = [article for article in search_results["value"]]
    return descriptions

