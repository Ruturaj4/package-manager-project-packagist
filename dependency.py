import json
import urllib.request
import time

url = "https://packagist.org/packages/"

with open("list.json", "r") as f:
    f = json.load(f)


def main():
    dic = {}
    count = 0
    total = len(f["packageNames"])
    print(f"Total packages/: {total}")
    for package in f["packageNames"]:
        #time.sleep(0.1)
        count += 1
        if count % 100 == 0:
            print(f"Done: {count}/{total}")
        temp = {}
        temp_two = {}
        print(package)
        try:
            data = urllib.request.urlopen(url + package + ".json").read()
            data = json.loads(data)
        except:
            continue

        try:
            temp_two["authors"] = data["package"]["versions"]["dev-master"]["authors"]
        except:
            temp_two["authors"] = []
        try:
            temp_two["require"] = list(data["package"]["versions"]["dev-master"]["require"])
        except:
            temp_two["require"] = []
        try:
            temp_two["stars"] = data["package"]["github_stars"]
        except:
            temp_two["stars"] = []
        try:
            temp_two["forks"] = data["package"]["github_forks"]
        except:
            temp_two["forks"] = []
        try:
            temp_two["downloads"] = data["package"]["downloads"]
        except:
            temp_two["downloads"] = {}

        temp[package] = temp_two
        dic.update(temp)
    with open("all.json", "w") as doc:
        json.dump(dic, doc)

if __name__=="__main__":
    main()
