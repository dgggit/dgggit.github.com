"""
pt_generator.py
v_1.0

This python program automatically generates one markdown file
into seperated md files into chronical-order split

Made by : Jinho Ko (dgggit.github.io)
"""

# Input!! Reads input.md in same directory
# write && at newline if year changes
# write & at newline if day changes

file = open('input.md', 'r')

MONTH = ['01', '02','03','04','05','06','07','08','09','10','11','12']
DAY = ['02','03','04','05','06','07','08','09']+[ str(i) for i in range(10, 29)] # day not using 01 for timezone diff
monthdayIndex = (0,0)
yearCnt = 999

def next(M, D, idx):
    mi, di = idx
    if len(D)-1 == di:
        return (mi+1,0)
    else:
        return (mi,di+1)

nowfile = None

for line in file:
    if line[0] == '&':
        if line[1] == '&': # new Year
            if nowfile is not None:
                nowfile.close()
            yearCnt+=1
            nowfile = open('./output/'+str(yearCnt)+'-01-02-pt.md','w')
            nowfile.write('---\ntag : presentation\n---\n')
        else:              # new Month/Day
            nowfile.close()
            monthdayIndex = next(MONTH,DAY,monthdayIndex)
            nowfile = open('./output/'+str(yearCnt)+'-'+str(MONTH[monthdayIndex[0]])+'-'+str(DAY[monthdayIndex[1]])+'-pt.md','w')
            nowfile.write('---\ntag : presentation\n---\n')
    else:
        nowfile.write(line)

nowfile.close()
file.close()
