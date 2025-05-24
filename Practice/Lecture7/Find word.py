word = "learning"
# search learning word in file
with open("file.txt","r") as f:
    data = f.read()
    if(data .find(word) != -1):
        print("Found")
    else:
        print("Not Found")