import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth 


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))

    response = None
    api_key = kwargs.get("apikey")
    try:
        # Call get method of requests library with URL and parameters
        if api_key:
            # Basic authentication GET
            response = request.get(url, params=kwargs, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
        else:
            # no authentication GET
            response = request.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"],
                                   state=dealer_doc["state"])
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list 
def get_dealer_reviews_from_cf(url, dealer_id, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealer_id)
    if json_result:
        # Get the row list in JSON as reviews
        reviews = json_result
        # For each reviews object
        for review in reviews:
            # Get its content in `doc` object
            review_doc = review
            # Create a DealerReview object with values in `doc` object
            sentiment = analyze_review_sentiments(review['review'])
            review_obj = DealerReview(id=review_doc["id"],name=review_doc["name"],dealership=review_doc["dealership"],
                                    review=review_doc["review"],purchase=review_doc["purchase"],
                                    purchase_date=review_doc["purchase_date"],car_make=review_doc["car_make"],
                                    car_model=review_doc["car_model"],car_year=review_doc["car_year"],
                                    sentiment=sentiment)
            results.append(review_obj)

    return results



# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(dealerreview):
    url = "https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/efbb37a3-8d01-4fbb-86cf-6139955ae50b"
    api_key = "1br6u_IwxWDB5MoFiprGq1K2Y29Dpk-120OuMF7xsRJc"
    params = dict()
    params["text"] = kwargs["text"]
    params["version"] = kwargs["version"]
    params["features"] = kwargs["features"]
    params["return_analyzed_text"] = kwargs["return_analyzed_text"]
    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                        auth=HTTPBasicAuth('apikey', api_key))
    get_request(url, api_key, params=params)


