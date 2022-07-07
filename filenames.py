import os

directory = 'static/images/documentaries/brakkebygrenda_to_2000/'
prefix = "../" + "/".join(directory.split("/")[1:])

output = []
for filename in os.listdir(directory):
    f = os.path.join(prefix, filename)
    output.append(f"{f}")

print()
for thang in output[::-1]:
    print(f"\t'{thang}',")
print()
