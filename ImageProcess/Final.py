import os
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)
import ProcessImage, Guess, CroppImage


class Final:

    def start(folder, endDir, model, bar):
        # replace "../"+"ImageProcess/" with folder if needed
        files = ProcessImage.getListOfFiles(folder)
        folders = []
        bar.setValue(25)
        for file in files:
            if "png" in file.split("."):
                # newdir = 'NameOfFile'
                newdir = endDir + file.split("/")[-1].split(".")[0]
                if not os.path.exists(newdir):
                    folders.append(newdir)
                    os.mkdir(newdir)
                    os.replace(file, newdir + "/" + file.split("/")[-1])
        # replace "../"+"ImageProcess/" with folder if needed
        files.clear()
        files = ProcessImage.getListOfFiles(endDir)
        newfiles = []
        for file in files:
            if "png" in file.split("."):
                newfiles.append(file)
        files.clear()
        for file in newfiles:
            CroppImage.cropp(file)
        newfiles.clear()
        bar.setValue(80)
        # replace "../"+"ImageProcess/" with folder if needed
        for pfolder in folders:
            words = ProcessImage.function(pfolder)
            Guess.guess(words, model)