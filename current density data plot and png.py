# Kyle Brittingham 3/31/22
# this script is for plotting current density data and saving it as .png
# data is in .csv format but maybe .xlsx is better to read from?
# Current data is A10:A
# Voltage data is B10:B
# not sure what C10:C is... but i think its error?
# D10:D is number of points averaged
import os
import numpy as np
import matplotlib.pyplot as plt
# PATH to files
mainfolder ='C:\\Users\\Kyle\\Documents\\College\\20xx_nano world\\NASA Cu-CNT\\current density data'

subfolder = '\\05-17-22\\'  # edit this and remember \ = \\

directory = os.fsencode(mainfolder + subfolder)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filepath = mainfolder+subfolder+filename
    if filename.endswith(".csv"):
        # dynamically find skip_header
        for i in range(0,30):
            try:            
                SKIP = i
                check = np.genfromtxt(filepath, dtype=float, delimiter=',', skip_header=SKIP, max_rows=30)
                if check[0,0] == 0:
                    print(i)
                    break
            except:
                pass

        # read in data from .csv, skip first 9-ish lines --EDIT skip_header as needed
        read_data = np.genfromtxt(filepath, dtype=float, delimiter=',', skip_header=SKIP)
        # format down to just current and voltage
        Current_density = np.delete(read_data,(2,3),1)
        # print(Current_density[0])

        # calculate resistance
        Current_density = np.insert(Current_density,2,0,1)  # zero everything
        for i in range(len(Current_density)-1):
            # if statement handles when current = 0 or -0,
            # resistance = 0 due to ohm's law V=IR??? OR should R = R(previous) bc its only for 0 and -0
            if Current_density[i+1,0] == 0:  # 0 = -0
                Current_density[i+1,2] = 0  # just for loop again to clean this up?
            else:  # this is a trailing slope formula
                Current_density[i+1,2] = (Current_density[i+1,1] - Current_density[i,1]) / (Current_density[i+1,0]-Current_density[i,0])

        # R = 0 clean up
        for i in range(len(Current_density)):
            # if statement handles when current = 0 or -0,
            if i == 0:  # the first point
                Current_density[i,2] = Current_density[i+1,2]  # first 0, choose the next R value and copy
            elif Current_density[i,0] == 0:
                Current_density[i,2] = Current_density[i-1,2]  # last 3 0's choose the previous R value and copy
            else:
                pass  # skip all non-0 current points

        # plot and format
        A = Current_density[:, 0]  # current in amps
        V = Current_density[:, 1]  # voltage in volts
        R = Current_density[:, 2]  # resistance in ohms

        fig, ax = plt.subplots(2)
        # plot IV
        ax[0].plot(A, V, 'b,-')
        plt.xlabel('current (A)')
        ax[0].set(ylabel='voltage (V)')
        ax[0].grid(which='major')
        # plot IR
        ax[1].plot(A, R, 'g,-')
        ax[1].set(ylabel='resistance (Ohm)')
        ax[1].grid()

        # export and .png or whatever
        plt.savefig(filepath+ '_IV_IR.png')
        print("Saved a file")
        plt.show(block=False)
        #######
        continue
    else:
        print("skip")
        continue
