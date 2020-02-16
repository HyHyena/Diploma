from PIL import Image
import os


def cropp(name):
    im = Image.open(name)
    # Size of the image in pixels (size of orginal image)
    # (This is not mandatory)
    # Setting the points for cropped image
    left = 400
    right = 460
    top = 220
    bottom = 280
    change = 86
    # Cropped image of above dimension
    # (It will not change original image)
    task = 'Task#'
    newdir = 'Images'
    os.mkdir('/'.join(name.split('/')[:-1]) + '/' + newdir)
    for i in range(24):
        for count in range(23):
            im.crop((left, top, right, bottom)).save('/'.join(name.split('/')[:-1]) + "/Images/" + task +
                                                     str(i) + '$' + str(count) + '.png')
            left += change
            right += change
        left = 400
        right = 460
        top += change
        bottom += change
