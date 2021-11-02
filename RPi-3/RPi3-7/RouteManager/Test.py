

for i in range(10):

    if i == 5:
        break

    print(i)


url = "/"
url_split = url.split("/")

print(len(url_split))

for i in range(len(url_split)):
    print(url_split[i])