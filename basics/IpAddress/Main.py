
ipAddress = ''
ipAddress = input("Enter the ip address : ")
if ipAddress[-1] != '.':
    ipAddress += '.'
segmentLength = 0
segment = 1

for item in ipAddress:
    if item == '.':
        print("found the segment {} and segment length is "
             "{}.".format(segment , segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1
