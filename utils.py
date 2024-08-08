import numpy as np
import cv2
import nibabel as nib
import requests
from io import BytesIO
import boto3 






directory = 'D:/Brain-Tumor-Classification-DataSet/image/'

# Tạo một client S3
s3 = boto3.client('s3')

def get_img_path(file_upload):
    byte = file_upload.read()
    file_name = file_upload.name
    # Đường dẫn lưu trữ tệp
    save_path = directory + file_name
    # Lưu tệp vào đường dẫn được chỉ định
    with open(save_path, "wb") as file:
        file.write(byte)
    return save_path

def dowload_from_s3(bucket_name, path):
    file_path = directory + path   # Tên tệp khi lưu trên máy tính của bạn

    # Tải tệp từ S3 và lưu vào máy tính
    s3.download_file(bucket_name, path, file_path)
    return file_path



def resize(data):
    img = np.zeros((155,128,128))
    for i in range(155):
         img[i] =  cv2.resize(data[i], (128, 128), interpolation=cv2.INTER_NEAREST)
    return img

def load_img(file_path):
    data = nib.load(file_path)
    data = np.asarray(data.dataobj)
    return data
    
def normalize(data: np.ndarray):
    data_min = np.min(data)
    return (data - data_min) / (np.max(data) - data_min)




