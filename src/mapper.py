import sys

for line in sys.stdin:
    line = line.strip()
    # date is specified in 15th to 23rd Byte
    date = line[15:23]
    # temp is specified in 87th to 92nd Byte
    temp = int(line[87:92])
    #  quality is specified in the 92nd Byte
    qlty = int(line[92])

    # need to discard invalid readings thus validating againts possible values for quality and invalid value for temp
    if qlty in [0, 1, 4, 5, 9] and temp != 9999:
        msg = '{}\t{}'.format(date, temp)
        print (msg)
      



