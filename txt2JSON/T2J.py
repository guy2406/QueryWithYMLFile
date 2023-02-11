import json
from datetime import datetime
import os


def line_not_header(split_Line,HEADER):
    print("i'm in the line_not header function")
    print("=========================")
    print(HEADER)
    values = split_Line[0].split(",")
    print(values[:len(HEADER)])
    res = {HEADER[i]: values[i] for i in range(len(HEADER))}
    return res

def header_to_dict(split_line):
    keyArr = []
    '''
    find position of value in list:
    Valid Until
    '''
    # pos = split_line.index("Region")
    # print(split_line[:pos])
    # return keyArr
    print(len(split_line))
    test = split_line[0].split(",")
    for word in test:
        if(word == "Valid Until"):
            keyArr.append(word)
            break
        keyArr.append(word)
    # print(keyArr)
    return keyArr



def convert() :
    finalArr = []
    print("in convert")
    cwd = os.getcwd()
    print(cwd)
    onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
    os.path.isfile(os.path.join(cwd, f))]
    print(onlyfiles)
    with open('tmp.txt','r', encoding='utf-8-sig') as outfile:
        content = outfile.read()
        splitcontent = content.splitlines()

    # Split each line by pipe
    lines = [line.split(' | ') for line in splitcontent]
    print(f"before sending to line_to_dict function {lines}")
    # Convert each line to dict
    isHEADER = True
    #lines = [line_to_dict(l,lineCounter) for l in lines]
    for l in lines:
        if isHEADER is True:
            keyRes = header_to_dict(l)
            isHEADER = False
            print("end of if")
            print(keyRes)
        else:
            if l[0].startswith(","):
                break
            print("got line_to_dict function")
            lineDict = line_not_header(l,keyRes)
            finalArr.append(lineDict)
    # current date and time
    now = datetime.now()


    s2 = now.strftime("%d_%m_%Y-%H_%M_%S")
    # dd/mm/YY H:M:S format
    print("s2:", s2)

    # Output JSON 
    with open(f"{s2}.json", 'w') as fout:
        json.dump(finalArr, fout, indent=4)
    return finalArr


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
    res = convert()
    print("%%%%%%%%%%%%%%%%%%\n")
    print(f"my final res is: \n{res}")
    print(len(res))