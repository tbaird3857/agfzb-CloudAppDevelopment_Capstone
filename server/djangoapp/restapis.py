import requests
import json
# import related models here
from .models import CarMake, CarModel, CarDealer, DealerReview 
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative

'''
9. Now, open the restapis.py file, and in the get_dealers_from_cf function, replace the line:

# Get its content in doc object

dealer_doc = dealer["doc"]

with the new line:

dealer_doc = dealer

This will update the way the dealer_doc variable retrieves the content from the dealer object.
'''

def get_request(url, params=None, **kwargs):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers, auth=HTTPBasicAuth('apikey', api_key), **kwargs)
    return response

def post_request(url, params=None, json_payload=None, **kwargs):
    response = requests.post(url, params=params, json=json_payload, **kwargs)
    return response

def get_dealers_from_cf(url, **kwargs):
    response = get_request(url, **kwargs)
    dealers_data = response.json()
    dealerships = []
    for dealer_data in dealers_data:
        dealer = CarDealer(
            id=dealer_data['id'],
            city=dealer_data['city'],
            state=dealer_data['state'],
            address=dealer_data['address'],
            zip=dealer_data['zip']
            # Add other attributes as needed
        )
        dealerships.append(dealer)
    return dealerships

def get_dealer_reviews_from_cf(url, dealerId):
    response = get_request(url, params={'dealerId': dealerId})
    reviews_data = response.json()
    reviews = []
    for review_data in reviews_data:
        review = DealerReview(
            id=review_data['id'],
            name=review_data['name'],
            dealership=review_data['dealership'],
            review=review_data['review'],
            purchase=review_data['purchase'],
            purchase_date=review_data.get('purchase_date', None),
            car_make=review_data.get('car_make', None),
            car_model=review_data.get('car_model', None),
            car_year=review_data.get('car_year', None)
        )
        reviews.append(review)
    return reviews

def analyze_review_sentiments(text):
    url = "https://your-watson-nlu-url/analyze"  # Replace with the actual Watson NLU URL
    params = {
        "text": text,
        "features": {
            "sentiment": {}
        }
    }
    response = get_request(url, params=params)
    sentiment_data = response.json()
    sentiment_label = sentiment_data['sentiment']['document']['label']
    return sentiment_label

