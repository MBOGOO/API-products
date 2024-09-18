import requests

def fetch_products(api_url):
    try:
        # Send a GET request to the API with a timeout
        response = requests.get(api_url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse JSON data
            
            # Print the JSON data for debugging
            print("API Response:", data)
            
            # Ensure 'products' key exists in the JSON data
            products = data.get('products', [])
            
            # Count products with brand 'Samsung', handling missing 'brand' keys
            samsung_products = [product for product in products if isinstance(product, dict) and product.get('brand') == 'Samsung']
            return len(samsung_products)  # Count the number of Samsung products
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred - {e}")
        return None

# Example usage
api_url = "https://dummyjson.com/products"
samsung_product_count = fetch_products(api_url)
if samsung_product_count is not None:
    print(f"Number of Samsung products: {samsung_product_count}")