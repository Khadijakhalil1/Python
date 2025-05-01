# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Mona",
    "age": 24,
    "is_student": False
}
print(person)
print(person["name"])         # Output: Alice
print(person.get("age"))      # Output: 30
print(person.get("city", "N/A"))  # Output: N/A (default if key not found)
person["city"] = "New York"     # Add new key-value
person["age"] = 30              # Update existing key
del person["is_student"]        # Deletes the key
age = person.pop("age")         # Removes key and returns value
