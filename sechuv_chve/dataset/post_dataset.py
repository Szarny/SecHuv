import requests
import glob
import json


URL = "http://localhost:8080/{}"

def main():
    directories = ["web", "mail", "other", "vuln"]

    for directory in directories:
        files = glob.glob("{}/*".format(directory))

        for file in files:
            print(file)
            with open(file, encoding='utf-8') as fp:
                data = json.load(fp)

                if directory != "vuln":
                    directory_ = "{}/case".format(directory)
                else:
                    directory_ = directory

                data_ = json.dumps(data, ensure_ascii=False)

                print(requests.post(URL.format(directory_), data=data_.encode("utf-8"), headers={'content-type': 'application/json'}).text)

main()