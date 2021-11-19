import sys

rowDate = None
date = None


maxTemp = -1000
for line in sys.stdin:
    line = line.strip()
    strsp = line.split('\t', 1)
    rowDate = strsp[0]
    temp = strsp[1]
    # rowDate, temperature = line.split('\t', 1)
    try:
        temp = int(temp)
    except:
        continue

    # Got a new value for the same date, update the maxTemp if temp is higher 
    if date == rowDate:
        if temp > maxTemp :
            maxTemp = temp

    # Print the max temp of previous date and proceed with next date
    else:
        if date:
            print('%s\t%d' % (date, maxTemp))
        # update new date and new maxTemp
        date = rowDate
        maxTemp = temp
        

if date == rowDate:
    print('%s\t%d' % (date, maxTemp))
