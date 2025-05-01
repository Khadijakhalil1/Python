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
