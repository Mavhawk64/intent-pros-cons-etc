import json
with open("lists.txt", "r") as f:
    # lists.txt like this:
    # Alpha:
    # - a
    # - b
    #
    # Beta:
    # - c
    # - d
    # ...

    # Transform to {"Alpha": {"pros": "","cons": "", "DealBreaker": "", "General Notes": "", "list": ["a": {"pros": "", "cons": "", "DealBreaker": "", "notes": ""}, ...]}, "Beta": ...}
    chunks = f.read().split("\n\n")
    data = {}
    for chunk in chunks:
        lines = chunk.split("\n")
        key = lines[0].strip()[:-1].strip()
        data[key] = {"General Pros": "", "General Cons": "",
                     "Class DealBreaker": "", "General Notes": "", "list": []}
        for line in lines[1:]:
            if line:
                data[key]["list"].append(
                    {line[2:].strip(): {"pros": "", "cons": "", "popularity": "", "DealBreaker": "", "notes": "", "source": ""}})
    # output.json indent4
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)
