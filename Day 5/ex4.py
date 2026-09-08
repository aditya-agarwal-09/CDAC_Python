"""

Scenario
An AI classification pipeline processes raw data inputs. Each raw input is a tuple of string annotations describing a product name, its price, and rating. The pipeline needs to clean, filter, and sort these records.

Problem Description
Write a function process_dataset(dataset) that processes a dataset using built-in higher-order functions (map, filter) and lambda expressions:

dataset is a list of tuples containing string records. Example:
[("Laptop", "Price: 1200", "Rating: 4.8"), ("Phone", "Price: 800", "Rating: 4.5")]
Your pipeline must execute the following sequential steps:
Parsing: From the incoming raw tuples, extract the product name (string), numeric price (float), and rating (float). (You can use string splitting or RegEx to isolate the numeric values).
Filtering: Use filter() with a lambda function to keep only items with a parsed price less than or equal to 1000.0.
Mapping: Use map() with a lambda function to transform the filtered entries into dictionaries of the following structure: {"product": <name>, "price": <float_price>, "score": <float_rating>}.
Sorting: Sort the resulting list of dictionaries in descending order of their score using sorted() with a lambda key selector. If two items have the same score, their relative order does not matter.
The function should return the sorted list of dictionaries.
Sample Input
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]

"""

def process_dataset(dataset):
    # Step 1: Parse the raw tuples
    parsed = map(
        lambda item: (
            item[0],
            float(item[1].split(":")[1].strip()),
            float(item[2].split(":")[1].strip())
        ),
        dataset
    )

    # Step 2: Keep items priced at <= 1000
    filtered = filter(lambda item: item[1] <= 1000.0, parsed)

    # Step 3: Convert to dictionaries
    mapped = map(
        lambda item: {
            "product": item[0],
            "price": item[1],
            "score": item[2]
        },
        filtered
    )

    # Step 4: Sort by score descending
    return sorted(mapped, key=lambda item: item["score"], reverse=True)
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]

result = process_dataset(data_input)

print(result)
