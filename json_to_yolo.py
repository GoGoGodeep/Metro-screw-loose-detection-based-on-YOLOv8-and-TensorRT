import json
import os

# images_tag分好的数据集地址
ImageSets_dir = r'E:\Segdata\ImageSets'
# json文件所在地址
json_dir = r'E:\Segdata\data_json'
# 主地址
base_dir = r'E:\Segdata'


for txt_name in os.listdir(ImageSets_dir):
    with open(os.path.join(ImageSets_dir, txt_name)) as txt:
        while True:
            img_name = txt.readline()   # '0000\n'
            if img_name == '':
                break
            json_name = img_name[:-1] + '.json' # 每行读取最后面有换行符

            with open(os.path.join(json_dir, json_name)) as f:
                data = json.load(f)

            image_path = data['imagePath']  # 读取json文件中的图片地址

            img_txt = open(os.path.join(base_dir, txt_name), 'a')
            img_txt.write(base_dir + image_path[2:] + '\n')     # json中的图片地址为..\\images\

            img_txt.close()

