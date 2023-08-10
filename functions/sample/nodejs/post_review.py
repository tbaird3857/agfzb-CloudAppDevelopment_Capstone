from cloudant.client import Cloudant
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF protection for demonstration purposes. Implement proper security in production.
def post_review(request):
    if request.method == 'POST':
        # Replace these with your actual Cloudant credentials
        cloudant_username = "your_cloudant_username"
        cloudant_password = "your_cloudant_password"
        cloudant_url = "https://your-cloudant-account.cloudant.com"

        try:
            # Parse the JSON data from the request body
            review_data = request.POST.get('review')
            
            if review_data is None:
                return JsonResponse({"error": "Missing 'review' data in the request"}, status=400)
            
            # Connect to the Cloudant service
            client = Cloudant(cloudant_username, cloudant_password, url=cloudant_url)
            client.connect()

            # Replace 'reviews' with the actual name of your database
            db_name = "reviews"
            db = client[db_name]

            # Save the review data to the Cloudant database
            review_doc = db.create_document(review_data)
            
            # Disconnect from the Cloudant service
            client.disconnect()

            if review_doc.exists():
                return JsonResponse({"message": "Review added successfully", "review_id": review_doc['_id']}, status=201)
            else:
                return JsonResponse({"error": "Failed to add review"}, status=500)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


