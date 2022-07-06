# import required module
import os
# assign directory
directory = 'static/images/frog'
prefix = "../images/frog"

# iterate over files in
# that directory
output = []
for filename in os.listdir(directory):
    f = os.path.join(prefix, filename)
    output.append(f"{f}")
print(output)
