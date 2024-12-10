# import csv

# # Load quotes from a CSV file
# def load_quotes(file_path):
#     quotes = []
#     with open(file_path, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             quotes.append(row)
#     return quotes

# # Load and display quotes
# if __name__ == "__main__":
#     file_path = "motivational_quotes.csv"
#     quotes = load_quotes(file_path)
#     for quote in quotes[:5]:  # Display the first 5 quotes
#         print(f"{quote['Quote']} - {quote['Author']} ({quote['Era']})")

import csv

def load_quotes(file_path):
    quotes = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quotes.append(row)
    return quotes

def display_menu():
    print("\nWelcome to the Motivational Quotes App!")
    print("Please choose an option:")
    print("1. Search quotes by category or interest")
    print("2. Search quotes by release era or background in history")
    print("3. Search quotes by author or attributed historical figures")
    print("4. Save a favorite quote")
    print("5. View favorite quotes")
    print("6. Exit")

def search_by_category(quotes):
    category = input("Enter a category or interest: ").strip().lower()
    results = [quote for quote in quotes if quote['Category'].strip().lower() == category]
    
    if results:
        print(f"\nQuotes under the category '{category}':")
        for quote in results:
            print(f"\"{quote['Quote']}\" - {quote['Author']} ({quote['Era']})")
    else:
        print(f"\nNo quotes found for the category '{category}'.")

def search_by_era(quotes):
    era = input("Enter a release era or background (e.g., '20th Century'): ").strip().lower()
    results = [quote for quote in quotes if quote['Era'].strip().lower() == era]

    if results:
        print(f"\nQuotes from the era '{era}':")
        for quote in results:
            print(f"\"{quote['Quote']}\" - {quote['Author']}")
    else:
        print(f"\nNo quotes found for the era '{era}'.")

def search_by_author(quotes):
    author = input("Enter an author or historical figure: ").strip().lower()
    results = [quote for quote in quotes if quote['Author'].strip().lower() == author]

    if results:
        print(f"\nQuotes by '{author}':")
        for quote in results:
            print(f"\"{quote['Quote']}\" ({quote['Era']})")
    else:
        print(f"\nNo quotes found for the author '{author}'.")

def save_favorite(quotes):
    try:
        quote_number = int(input("Enter the quote number to save as favorite: "))
        if 1 <= quote_number <= len(quotes):
            favorite = quotes[quote_number - 1]
            with open("favorites.csv", mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Quote", "Author", "Category", "Era"])
                if file.tell() == 0:  # Check if the file is empty
                    writer.writeheader()
                writer.writerow(favorite)
            print(f"\nQuote saved to 'favorites.csv':\n\"{favorite['Quote']}\" - {favorite['Author']}")
        else:
            print("\nInvalid quote number. Please try again.")
    except ValueError:
        print("\nPlease enter a valid number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def view_favorites():
    try:
        with open("favorites.csv", mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            favorites = list(reader)

            if favorites:
                print("\nYour Favorite Quotes:")
                for idx, favorite in enumerate(favorites, start=1):
                    print(f"{idx}. \"{favorite['Quote']}\" - {favorite['Author']} ({favorite['Era']}) [Category: {favorite['Category']}]")
            else:
                print("\nYou have no saved favorite quotes yet.")
    except FileNotFoundError:
        print("\nNo favorites file found. Save some quotes first!")
    except Exception as e:
        print(f"\nAn error occurred while loading favorites: {e}")

def main():
    file_path = "motivational_quotes.csv"
    quotes = load_quotes(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            search_by_category(quotes)
        elif choice == '2':
            search_by_era(quotes)
        elif choice == '3':
            search_by_author(quotes)
        elif choice == '4':
            print("\nAvailable Quotes:")
            for idx, quote in enumerate(quotes, start=1):
                print(f"{idx}. \"{quote['Quote']}\" - {quote['Author']}")
            save_favorite(quotes)
        elif choice == '5':
            view_favorites()
        elif choice == '6':
            print("\nThank you for using the Motivational Quotes App! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()