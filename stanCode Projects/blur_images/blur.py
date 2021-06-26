"""
File: blur.py
Name: Sharlene Chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: must be an image file
    :return: a new image that is blurred
    """
    new_img = SimpleImage.blank(img.width, img.height) #creating new image
    for x in range(img.width):
        for y in range(img.height):
            if x == 0 and y == 0: #for the four corners
                minx,maxx, miny, maxy = x, x+1, y, y+1
                #setting the coordinates of their neighbors that will be looped later
            elif x == img.width-1 and y == 0:
                minx,maxx, miny, maxy = x-1, x, y, y+1
            elif x == 0 and y == img.height-1:
                minx, maxx, miny, maxy = x, x+1, y-1, y
            elif x == img.width-1 and y == img.height-1:
                minx, maxx, miny, maxy = x-1, x, y-1, y
            elif x == 0 and (y != 0 and y != img.height-1): #for the four sides
                minx, maxx, miny, maxy = x, x+1, y-1, y+1
            elif (x != 0 and x != img.width-1) and y == 0:
                minx, maxx, miny, maxy = x-1, x+1, y, y+1
            elif x == img.width-1 and y!= 0 and y!= img.height-1:
                minx, maxx, miny, maxy = x-1, x, y-1, y+1
            elif x != 0 and x != img.width-1 and y == img.height-1:
                minx, maxx, miny, maxy = x-1, x+1, y-1, y
            else: #pixels in the middle
                minx, maxx, miny, maxy = x-1, x+1, y-1, y+1
            rtotal = gtotal = btotal = 0
            count = 0
            for i in range(minx,maxx+1): #looping through all the neighboring pixels
                for j in range(miny,maxy+1):
                    r,g,b = img.get_pix(i,j)
                    rtotal = rtotal + r
                    gtotal = gtotal + g
                    btotal = btotal + b
                    count += 1
            new_r = rtotal // count
            new_g = gtotal // count
            new_b = btotal // count
            new_img.set_rgb(x,y, new_r,new_g,new_b) #setting the rgb for the new img
    return new_img


def main():
    """
    TODO: The function takes in the smiley-face image and blurs it by averaging
    the neightboring pixels and substituting each pixel with the new neightbor
    average. The image must be in the same directory as this module.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5): #can change the blur factor to blur further
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
