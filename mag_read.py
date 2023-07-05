import os
import matplotlib.pyplot as plt

#class SQuID():
#    def __init__(self, filename)
#        self.filename = filename


if __name__ == "__main__":
    directory = "Blackmore_Magnetometry/100_Parr/"
    directory = "Blackmore_Magnetometry/001_Parr/"
    directory = "Blackmore_Magnetometry/010_Parr/"
    Filenames = []
    for file in  os.listdir(directory):
        if file.endswith(".dat") == True:
            Filenames.append(file)
##    filename = "Blackmore_Magnetometry/" +\
#               "100_Parr/" +\
#               "Mag001_100_InPlane_EdgeParr_Hysteresis_110K_3T.dat"
    for filename in Filenames:
        file = open(os.path.join(directory,filename))
        Lines = file.readlines()
        col_names = []
        field = []
        moment = []
        for _, line in enumerate(Lines):
            
            if _ == 44:
                col_names = line.strip().split(",")
            elif _ > 44:
                field.append( float(line.strip().split(",")[3]))
                moment.append(float(line.strip().split(",")[4]))
    
        plt.plot(field, moment)
        plt.title(filename)
        plt.savefig(directory + "plots/" + filename[:-3] + "png")
        plt.close()
