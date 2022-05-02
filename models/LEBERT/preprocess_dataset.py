import re
import os

mode = "test"

read_path = "data/dataset/NER/edu/" + mode + ".csv"
save_path = "data/dataset/NER/edu/" + mode + "_withE.csv"

with open(read_path, "r") as f_to_read:
    file = f_to_read.read()
    a = file.split('\n')
    for i in range(len(a)):
        if a[i] == '':
            continue
        matchObj = re.match(r'(\S) I-(\S*)', a[i])
        if matchObj != None:
            if not re.match(r'(\S) I-(\S*)', a[i+1]):
                # print(matchObj.group(1))
                # print(matchObj.group(2))
                a[i] = matchObj.group(1) + ' E-' + matchObj.group(2)

    with open(save_path, "w") as f_to_write:
        for line in a:
            f_to_write.write(line)
            f_to_write.write('\n')

with open(save_path, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()
