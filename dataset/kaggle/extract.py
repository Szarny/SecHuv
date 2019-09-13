import csv

i = 1

with open('spam.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        typ, body = row[0], row[1]

        if typ == "spam":
            with open("spam/{0:03d}_kagglespam.txt".format(i), "w") as g:
                g.write(body)
                i += 1