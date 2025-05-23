with open("practice.txt","r") as f:
    data=f.read()

new_Data=data.replace("Java","Python")
print(new_Data)

with open("practice.txt","w") as f:
    f.write(new_Data)

