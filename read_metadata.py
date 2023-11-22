# https://stackoverflow.com/questions/12521525/reading-metadata-with-python

import win32com.client

sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
ns = sh.NameSpace(r'D:\Videos\Battlefield 2042\webm\9k_flank.webm')
colnum = 0
columns = []
while True:
    colname = ns.GetDetailsOf(None, colnum)
    if not colname:
        break
    columns.append(colname)
    colnum += 1

for item in ns.Items():
    print(item.Path)
    for colnum in range(len(columns)):
        colval = ns.GetDetailsOf(item, colnum)
        if colval:
            print('\t', columns[colnum], colval)
