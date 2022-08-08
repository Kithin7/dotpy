# Kyle Brittingham 5/18/22
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
Folder_list = ("02-15-22","02-17-22","02-18-22","02-24-22","03-01-22","03-02-22","03-03-22","03-04-22","03-07-22","03-09-22","03-10-22","03-15-22","03-17-22","03-23-22","03-25-22","03-28-22","05-16-22","05-17-22","05-20-22",)

for L in range(0, len(Folder_list)): # iterates through all folders listed above
    subfolder = '\\'+Folder_list[L]+'\\'  # updates target each loop
    print(Folder_list[L])

    directory = os.fsencode(mainfolder + subfolder)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filepath = mainfolder + subfolder + filename
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
            CD = np.delete(read_data,(2,3),1)
            CD = np.insert(CD,2,0,1)  # zero everything

            # calculate resistance - use finite difference
            for j in range(len(CD)):
                # beginning case, forward dif, acc 3 (using 4 terms)
                if j < 1:
                    CD[j,2] = (-11/6*CD[j,1] + 3*CD[j+1,1] - 3/2*CD[j+2,1] + 1/3*CD[j+3,1]) / (CD[j+1,0] - CD[j,0])
                # ending case, backward dif, acc 3 (using 4 terms)
                elif j >= (len(CD)-2):
                    CD[j,2] = (-1 / 3 * CD[j - 3, 1] + 3 / 2 * CD[j - 2, 1] - 3 * CD[j - 1, 1] + 11 / 6 * CD[j, 1]) / (CD[j, 0] - CD[j - 1, 0])
                # Max/min current cusp
                elif CD[j,0] == max(CD[:,0]) or CD[j,0] == min(CD[:,0]):
                    CD[j,2] = -1234567890 # placeholder
                # middle cases
                elif CD[j,0] > CD[j-1,0]:
                    CD[j,2] = (1/12*CD[j-2,1] - 2/3*CD[j-1,1] + 2/3*CD[j+1,1] - 1/12*CD[j+2,1]) / (CD[1,0] - CD[0,0])
                else:
                    CD[j,2] = (1/12*CD[j-2,1] - 2/3*CD[j-1,1] + 2/3*CD[j+1,1] -1/12*CD[j+2,1]) / (CD[0,0] - CD[1,0])

            # find and remove cusp points at max/min
            CD_trim = CD
            for k in range(len(CD_trim)-6):
                if CD_trim[k,0] == 0 or CD_trim[k,2] == -1234567890:
                    CD_trim = np.delete(CD_trim,k,0)
            for k in range(len(CD_trim)-1):
                if CD_trim[k,0] == 0 or CD_trim[k,2] == -1234567890:
                    CD_trim = np.delete(CD_trim,k,0)

            # organize for ease
            A = CD_trim[:,0]  # current in amps
            V = CD_trim[:,1]  # voltage in volts
            R = CD_trim[:,2]  # resistance in ohms

            # plot and format
            fig, ax = plt.subplots(2)
            # plot IV
            ax[0].plot(A, V, 'b,-')
            plt.xlabel('Current (A)')
            ax[0].set(ylabel='Voltage (V)')
            # ax[0].set_ylim(min(CD[:,1]), max(CD[:,1]))
            ax[0].grid(which='major')
            # plot IR
            ax[1].plot(A, R, 'g,-')
            ax[1].set(ylabel='Resistance (Ohm)')
            # ax[1].set_ylim(0, 1.05*max(CD_trim[:,2]))
            ax[1].grid()

            # export as .png or whatever
            plt.savefig(filepath+ '_IV-IR_finite-dif.png')
            print("Saved a file")
            plt.show(block=False)
            #######
            continue
        else:
            print("skip")
            continue
