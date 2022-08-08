# Kyle Brittingham 6/3/22
# this script is for plotting current density data and saving it as .png
# data is in .csv format
# Current data is A
# Voltage data is B
# not sure what C is... but i think its error?
# D is number of points averaged aka 32
# Current goes from 0 to max, to 0, to -0, to -1*max, and finally to 0
import os
import numpy as np
import matplotlib.pyplot as plt
# PATH to files
mainfolder ='C:\\Users\\Kyle\\Documents\\College\\20xx_nano world\\NASA Cu-CNT\\current density data'
#Folder_list = ("02-15-22","02-17-22","02-18-22","02-24-22","03-01-22","03-02-22","03-03-22","03-04-22","03-07-22","03-09-22","03-10-22","03-15-22","03-17-22","03-23-22","03-25-22","03-28-22","05-16-22","05-17-22","05-20-22","06-16-22","06-21-22")
Folder_list = ("06-21-22","06-22-22")

for L in range(0, len(Folder_list)):  # iterates through all folders listed above
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

            # read in data from .csv, skip first 9-ish lines
            Read_data = np.genfromtxt(filepath, dtype=float, delimiter=',', skip_header=SKIP)
            # format down to just current and voltage
            CD = np.delete(Read_data,(2,3),1)
            CD = np.insert(CD,2,0,1)  # zero everything

            # calculate resistance using finite difference - np.gradient or np.diff might be useful
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

            # find and remove cusp points at beginning/max/min/end
            CD_trim = CD # copy matrix - idk why
            for k in range(len(CD_trim)-6):
                if CD_trim[k,0] == 0 or CD_trim[k,2] == -1234567890:
                    CD_trim = np.delete(CD_trim,k,0)
            for k in range(len(CD_trim)-1): #repeated bc double 0 in middle
                if CD_trim[k,0] == 0 or CD_trim[k,2] == -1234567890:
                    CD_trim = np.delete(CD_trim,k,0)

            # organize for ease
            A = CD_trim[:,0]*1000  # current in mA
            V = CD_trim[:,1]  # voltage in Volts
            R = CD_trim[:,2]  # resistance in Ohms
            P = A*V           # power in mW

            # plot IV
            ax1 = plt.subplot(311)
            ax1.plot(A, V, 'b,-')
            ax1.set_ylabel('Voltage (V)')
            ax1.minorticks_on()
            ax1.grid(which='major', alpha=0.7)
            ax1.grid(which='minor', alpha=0.15)
            ax1.tick_params('x', labelbottom=False)

            # plot IP
            ax2 = plt.subplot(312)
            ax2.plot(A, P, 'r,-')
            ax2.set_ylabel('Power (mW)')
            ax2.minorticks_on()
            ax2.grid(which='major', alpha=0.7)
            ax2.grid(which='minor', alpha=0.15)
            ax2.tick_params('x', labelbottom=False)

            # plot IR
            ax3 = plt.subplot(313)
            ax3.plot(A, R, 'g,-')
            ax3.set_ylabel('Resistance (Ohm)')
            ax3.set_xlabel('Current (mA)')
            ax3.minorticks_on()
            ax3.grid(which='major', alpha=0.7)
            ax3.grid(which='minor', alpha=0.15)

            # export as .png or whatever
            plt.savefig(filepath+'_IV-IP-IR.png')
            print("Saved a file")
            plt.close()
        else:
            continue # that's all folks