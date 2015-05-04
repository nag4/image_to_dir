# -*- coding: utf-8 -*- 

from PIL import Image
import os
import shutil

user_name = os.getlogin()
# image/hoge.jpg, image/fuga.png, etc...
src_dir = "/Users/" + user_name + "/Desktop/image/"
# create dst_dir/yyyymmdd/
dst_dir = "/Users/" + user_name + "/Desktop/dst_dir/"

if os.path.exists(dst_dir) == False:
    os.mkdir(dst_dir)

for root, dirs, files in os.walk(src_dir):
    for filename in files:
        try:
            image_info = Image.open(src_dir + filename)
            # 36867 : EXIF DateTimeOriginal
            date = image_info._getexif()[36867]
            yyyy, mm, dd = date[:4], date[5:7], date[8:10]
            yyyymmdd_dir = os.path.join(dst_dir, yyyy + mm + dd)
            if os.path.exists(yyyymmdd_dir) == False:
                os.mkdir(yyyymmdd_dir)
            dst = os.path.join(yyyymmdd_dir, filename)
            if os.path.exists(dst) == False:
                shutil.copy2(src_dir + filename, dst)
        except Exception as e:
            # .DS_Store must Die
            print filename + ' is fail.'
