import json
with open("output_.json", "r") as f:
    data = json.load(f)
    for key, value in data.items():
        for t in value["list"]:
            for llave, valor in t.items():
                print(valor["source"])
                x = input("Is this source correct? y/n ")
                if x == "n":
                    valor["source"] = input("Enter the correct source: ")

# dump the data back to the file indent=4
json.dump(data, open("output_.json", "w"), indent=4)
