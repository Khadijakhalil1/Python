dec={
    "Name":"Khadija",
    "class":"BSCS",
    "Age": 20,
    "Gender":"Female",
    "Fav Sub" :
    {
"Math",
"comp"
    }
}
print(dec)
print(type(dec))
# Dictionary Methods
# Keys
print(list(dec.keys()))
# Print Values
print(dec.values())
# items
print(dec.items())
new_dic={
    "Name":"Horia",
    "Age" : "21"
}
dec.update(new_dic)
print(dec)