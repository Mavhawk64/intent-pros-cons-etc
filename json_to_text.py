import json
with open("output_.json", "r") as f:
    data = json.load(f)
    # output.txt
    with open("output_.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}:\n")
            for llave, valor in value.items():
                if llave == "list":
                    continue
                f.write(f"\t\t* {llave}: {valor}\n")
            for item in value["list"]:
                for item_key, item_value in item.items():
                    f.write(f"\t\t{item_key}:\n")
                    for key, value in item_value.items():
                        f.write(f"\t\t\t\t- {key}: {value}\n")
            f.write("\n")
