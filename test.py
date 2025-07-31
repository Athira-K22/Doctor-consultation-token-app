# This file is used for test commits
import pprint

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "cycling", "hiking"],
    "education": {
        "undergrad": {"university": "ABC", "year": 2015},
        "postgrad": {"university": "XYZ", "year": 2018}
    }
}

print(data)
# Output is all on one line, hard to read for big structures


print("\n the start of pretty print pprint")
pprint.pprint(data)
# Output is indented and easier to read