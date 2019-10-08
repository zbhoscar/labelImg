import os.path as osp
import shutil

# YOLO format
model_file = '/home/zbh/Downloads/anoma_only_test/Arrest001_x264/01335.txt'


extend_start = '01185'
extend_end = '01485'
suffix = '.txt'

extend_list = [osp.join(osp.dirname(model_file), str(i).zfill(5) + suffix)
               for i in range(int(extend_start), int(extend_end) + 1)]

for i in extend_list:
    if i != model_file:
        shutil.copyfile(model_file, i)
