import requests

# URL de l'API Flask
API_URL = "http://localhost:5000/predict"

def predict(image_url):
    try:
        response = requests.post(API_URL, data={'url': image_url})
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None

def main():
    while True:
        image_url = input("Enter the image URL (or press Enter to exit): ").strip()
        
        if not image_url:
            print("Exiting...")
            break
        
        prediction = predict(image_url)
        
        if prediction:
            class_id = prediction.get('class_id')
            class_name = prediction.get('class_name')
            print(f"Class ID: {class_id}")
            print(f"Class Name: {class_name}")
        else:
            print("Failed to get prediction. Please check the URL and try again.")

if __name__ == "__main__":
    main()
