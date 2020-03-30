import sys
from ruler import Ruler



DATASET = sys.argv[1]

with open(DATASET, "r") as data:
    lines = data.readlines()
    l = len(lines)//2
    for i in range(l):
        line1 = lines[2*i]
        line2 = lines[2*i+1]
    if line1[-1]== '\n':
        line1 = line1[0:len(line1)-1]
    if line2[-1]== '\n':
        line2 = line1[0:len(line2)-1]

    R = Ruler(line1,line2)
    R.compute()
    print(f'=========== comparaison n° {i} -- distance = {R.distance}')
    top, bot = R.report()
    print(top)
    print(bot)
