import cv2, os, pickle, random, natsort
from PIL import Image
import numpy as np
import scale
import Alphabet

count = 0
dataset = list()
dataset_test = list()


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    # print(listOfFile)

    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:

        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def deleteAlfaCh(image_name):
    """ Deleting alfa channel from an image and saving into new
    read new image, make mask of where the transparent bits are,
    replace areas of transparency with white and not transparent,
    new image without alpha channel...
    :param image_name: name of the next image
    :return: new saved image
    """
    image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
    global count
    trans_mask = image[:, :, 3] == 0

    image[trans_mask] = [255, 255, 255, 255]
    new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)


#    cv2.imwrite(new_image_name + str(count) + '.png', new_img)
#    count += 1


def scaleImage(name):
    """
    Scaling image from any size to 28x28 and reformatting it
    into numpy array
    :param name: name of the next image
    :return: scaled image in the numpy array form
    """
    global dataset, count, dataset_test
    img = Image.open(name)

    bbox = Image.eval(img, lambda px: 255 - px).getbbox()
    if bbox is None:
        return np.zeros(784, )
    # Original lengths of sides
    widthlen = bbox[2] - bbox[0]
    heightlen = bbox[3] - bbox[1]
    # New lengths of sides
    if heightlen > widthlen:
        widthlen = int(20.0 * widthlen / heightlen)
        heightlen = 20
    else:
        heightlen = int(20.0 * widthlen / heightlen)
        widthlen = 20
    if widthlen is 0 or heightlen is 0:
        return np.zeros(784, )
    # Starting point for drawing
    hstart = int((28 - heightlen) / 2)
    wstart = int((28 - widthlen) / 2)
    # Scaled image
    img_temp = img.crop(bbox).resize((widthlen, heightlen), Image.NEAREST)
    # Transforming into new white image
    new_img = Image.new('L', (28, 28), 255)
    new_img.paste(img_temp, (wstart, hstart))

    # Converting into numpy array and normalizing
    imgdata = list(new_img.getdata())
    img_array = np.array([(255.0 - x) / 255.0 for x in imgdata])
    #    new_img.show()
    return img_array


#     a = 0
#     for el in Alphabet:
#         if name.split('/')[1] == el.name:
#             a = el.value
#     if count < 20:
#         dataset_test.append([img_array, a])
#     else:
#         dataset.append([img_array, a])
#     count += 1
#     if a != dataset_test[len(dataset_test)-1][1]:
#         count = 0

def build_dataset(directory_name):
    """
    Building new dataset
    :return: 4 files containing labels and features
    """
    listOfFiles = getListOfFiles(directory_name)
    for elem in listOfFiles:
        if ".DS_Store" in elem.split("/"):
            pass
        else:
            scaleImage(elem)
    X = []
    y = []
    X_test = []
    y_test = []
    random.shuffle(dataset)
    random.shuffle(dataset_test)
    for features, label in dataset:
        X.append(features)
        y.append(label)
    for features, label in dataset_test:
        X_test.append(features)
        y_test.append(label)

    pickle_out = open("X.pickle", "wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

    pickle_out = open("X_test.pickle", "wb")
    pickle.dump(X_test, pickle_out)
    pickle_out.close()

    pickle_out = open("y_test.pickle", "wb")
    pickle.dump(y_test, pickle_out)
    pickle_out.close()


def function(directory_name):
    elements = []
    numbers = []
    listOfFiles = getListOfFiles(directory_name)
    # Sorting files in a numerical order
    listOfFiles = natsort.natsorted(listOfFiles)
    for elem in listOfFiles:
        name = elem.split('/')
        if 'Images' in name:
#            file = name[2].split('$')[0].split('#')
            if ".DS_Store" in elem.split("/"):
                pass
            else:
                elements.append(scaleImage(elem))
    pickle_out = open(directory_name + "/words.pickle", "wb")
    pickle.dump(elements, pickle_out)
    pickle_out.close()
    return directory_name + "/words.pickle"

def gettxts(dir):
    elements = []
    numbers = []
    listOfFiles = getListOfFiles(dir)
    # Sorting files in a numerical order
    listOfFiles = natsort.natsorted(listOfFiles)
    for elem in listOfFiles:
        name = elem.split('.')
        if 'txt' in name:
            if ".DS_Store" in elem.split("/"):
                pass
            else:
                elements.append(elem)
    return elements