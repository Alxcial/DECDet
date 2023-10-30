# coding=utf-8
import os
from mmdet.apis import init_detector
from mmdet.apis import inference_detector
from mmdet.apis import show_result_pyplot
import os
import time
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# 模型配置文件
config_file = '../../.py'

# 预训练模型文件
checkpoint_file = '../../../.pth'
# 通过模型配置文件与预训练文件构建模型
model = init_detector(config_file, checkpoint_file, device='cuda:0')
# 测试单张图片并进行展示
img = r'../../.png'
start = time.time()
result = inference_detector(model, img)
end = time.time()
show_result_pyplot(model, img, result)
print("程序的运行时间为：{}".format(end-start))



