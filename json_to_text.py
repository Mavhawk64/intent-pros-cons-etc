import json
with open("output_.json", "r") as f:
    data = json.load(f)
    # output.txt
    with open("output_.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}:\n")
            for llave, valor in value.items():
                if llave == "Technologies":
                    continue
                f.write(f"\t\t* {llave}: {valor}\n")
            for item in value["Technologies"]:
                name = item["name"]
                f.write(f"\t\t{name}:\n")
                for llave, valor in item.items():
                    if llave == "name":
                        continue
                    f.write(f"\t\t\t\t- {llave}: {valor}\n")
            f.write("\n")
