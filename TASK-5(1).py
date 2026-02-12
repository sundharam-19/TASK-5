# Sample list of dictionaries
people = [
    {"name": "prabha", "age": 25},
    {"name": "sundhar", "age": 17},
    {"name": "siva", "age": 30},
    {"name": "Dinesh", "age": 15},
    {"name": "mano", "age": 19}
]
try:
    # Step 1: Filter people aged 18 or older
    adults = list(filter(lambda person: isinstance(person.get("age"), int) and person["age"] >= 18, people))
    # Step 2: Map to extract only names
    adult_names = list(map(lambda person: person.get("name", ""),adults))
    print("Adult Names:",adult_names)
    print("Adults Details:\n",adults)
except Exception as e:
    print(f"An error occurred: {e}")
