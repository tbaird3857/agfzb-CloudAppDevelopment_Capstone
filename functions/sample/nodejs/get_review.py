from cloudant.client import Cloudant
from cloudant.query import Query
from django.http import JsonResponse

def get_reviews(request):
    # Replace these with your actual Cloudant credentials
    cloudant_username = "your_cloudant_username"
    cloudant_password = "your_cloudant_password"
    cloudant_url = "https://your-cloudant-account.cloudant.com"

    # Retrieve the dealerId parameter from the request
    dealer_id = request.GET.get('dealerId', None)
    if dealer_id is None:
        return JsonResponse({"error": "Missing 'dealerId' parameter"}, status=400)

    # Connect to the Cloudant service
    client = Cloudant(cloudant_username, cloudant_password, url=cloudant_url)
    client.connect()

    # Replace 'reviews' with the actual name of your database
    db_name = "reviews"
    db = client[db_name]

    # Create a query to retrieve reviews for the given dealerId
    query = Query(db, selector={"dealerId": dealer_id})

    # Execute the query and retrieve the results
    results = query(limit=100)['docs']  # Adjust the limit as needed

    # Disconnect from the Cloudant service
    client.disconnect()

    if not results:
        return JsonResponse({"error": f"No reviews found for dealerId: {dealer_id}"}, status=404)

    formatted_reviews = []
    for review in results:
        formatted_review = {
            "id": review.get('_id'),
            "name": review.get('name'),
            "dealership": review.get('dealerId'),
            "review": review.get('review'),
            "purchase": review.get('purchase', False),
            "purchase_date": review.get('purchase_date', ''),
            "car_make": review.get('car_make', ''),
            "car_model": review.get('car_model', ''),
            "car_year": review.get('car_year', '')
        }
        formatted_reviews.append(formatted_review)

    return JsonResponse({"reviews": formatted_reviews})

