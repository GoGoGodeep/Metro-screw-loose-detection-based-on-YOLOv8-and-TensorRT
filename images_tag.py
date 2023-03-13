import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--json_path', default=r"E:\Segdata\data_json", type=str, help="input json label path")
parser.add_argument('--txt_path', default=r"E:\Segdata\ImageSets", type=str, help="output txt label path")
opt = parser.parse_args()

trainval_percent = 0.9
train_percent = 0.7     # 这里的train_percent是指占trainval_percent中的
jsonfilepath = opt.json_path
txtsavepath = opt.txt_path
total_json = os.listdir(jsonfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_json)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:
    name = total_json[i][:-5] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()