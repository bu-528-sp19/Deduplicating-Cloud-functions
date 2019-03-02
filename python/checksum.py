import hashlib

def calculate_checksum(file):
    hash_obj = md5(file)
    #print("The checksum of the image is", hash_obj)
    return hash_obj

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == "__main__":
    calculate_checksum("a.jpg")