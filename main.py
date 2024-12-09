import csv

# Load quotes from a CSV file
def load_quotes(file_path):
    quotes = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quotes.append(row)
    return quotes

# Load and display quotes
if __name__ == "__main__":
    file_path = "motivational_quotes.csv"
    quotes = load_quotes(file_path)
    for quote in quotes[:5]:  # Display the first 5 quotes
        print(f"{quote['Quote']} - {quote['Author']} ({quote['Era']})")