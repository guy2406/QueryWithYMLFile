import json
import os
import txt2JSON.T2J

def openJsonFile():
    # /Users/guyweiss/Scripts/Query/Final/txt2JSON
    l_of_json = []
    cwd = os.getcwd()
    print(cwd)
    res = []

    # Iterate directory
    for path in os.listdir(cwd):
        # check if current path is a file
        if os.path.isfile(os.path.join(cwd, path)):
            # res.append(path)
            if path.endswith(".json"):
                res.append(path)
    print(res)
    if res == []:
        print("i'm in the if no json file")
        txt2JSON.T2J.convert()
        exit(1)
        
    print("in open Function!!!!")
    print(f'list of all json files:-->{res}')
    # with open('txt2JSON/10_02_2023-07_47_20.json', 'r') as f:
    with open('%s'%res[0], 'r') as f:
        data = json.load(f)
    return data

def read_all():
    test = openJsonFile()
    print("check this -->")
    print(len(test))
    return test

def get_headers():
    find = openJsonFile()
    print("in get header function")
    print(type(find[0]))
    print(find[0])
    print("\n\n&&&&&&&&&&")
    print(find[0].keys())
    # return find[0]
    return find[0].keys()

# Partner name": "Euplink"
def read_one():
    find = openJsonFile()
    filtered_arr = [p for p in find if p["Partner name"] == "Euplink"]
    #print("Euplink Count")
    print(type(filtered_arr))
    print(len(filtered_arr))
    return filtered_arr