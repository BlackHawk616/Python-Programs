# Copying a text File into another 

def copy(path):
    with open(path, "r") as src:
        with open(path, "w") as dst:
            dst.write(src.read())
