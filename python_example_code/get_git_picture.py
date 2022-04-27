from PIL import Image

im = Image.open("1.jpeg")
images = []
images.append(Image.open('2.jpeg'))
images.append(Image.open('3.jpg'))
im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")