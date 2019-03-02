from PIL import Image

#, (720,720), (1600,1600)
def create_thumbnail(img):
    sizes = [(120,120)]
    files = [img]
    for image in files:
        for size in sizes:
            im = Image.open(image)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save("out"+str(size[0])+".jpg")
            print("Thumbnail generated "+"out"+str(size[0])+".jpg")

if __name__ == "__main__":
    create_thumbnail("a.jpg")