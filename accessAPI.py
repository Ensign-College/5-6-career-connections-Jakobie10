import requests 
import json 

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def get_chapter_summary(book, chapter):
    url = f"{base_url}{book}/{chapter}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        
        data = response.json()
        summary = data.get('chapter', {}).get('summary')
        
        if summary:
            return summary
        else:
            print("No summary available for this chapter.")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    while True:
        book = input("Which book of the Book of Mormon would you like? ")
        chapter = input(f"Which chapter of {book} are you interested in? ")
        
        summary = get_chapter_summary(book.lower().replace(" ", ""), chapter)
        
        if summary:
            print(f"Summary of {book} chapter {chapter}:")
            print(f"--{summary}")
        else:
            print("Failed to retrieve data. Please check the book and chapter and try again.")
        
        another = input("Would you like to view another (Y/N)? ").strip().lower()
        if another != 'y':
            break
    
    print("Thank you for using Book of Mormon Summary Tool!")

# Directly calling the main function
main() 
