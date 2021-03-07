import GroupProject.Cimpl as Cimpl

img = Cimpl.load_image("./CimpL-Demo/green_image.jpg")
w = img.get_width()
h = img.get_height()
count = 0
for i in range(w):
    for j in range(h):
        col = img.get_color(i, j)
        r, g, b = col
        temp = r
        r = g
        g = temp
        img.set_color(i, j, color=Cimpl.Color(r, g, b))
        if count % 10000 == 0:
            img.show()
        count += 1
