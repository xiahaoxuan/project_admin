from fdfs_client.client import Fdfs_client, get_tracker_conf
from django.conf import settings
import os

if __name__ == '__main__':
    # tracker_path = get_tracker_conf('')

    tracker_path = get_tracker_conf(conf_path=settings.FASTDFS_PATH)
    client = Fdfs_client(tracker_path)
    ret = client.upload_by_filename('/Users/zhishi/Desktop/picture/2029233.jpg')
    print(ret)

'''
mysql -h127.0.0.1 -uroot -pmysql meiduo_tbd39 < goods_data.sql
{
    'Storage IP': '192.168.47.128',
    'Group name': 'group1',
    'Uploaded size': '8.00KB',
    'Status': 'Upload successed.',
    'Local file name': '/home/python/Desktop/1.jpg',
    'Remote file_id': 'group1/M00/00/00/wKgvgFyVsQKANIKnAAAhg8MeEWU833.jpg'
}

'''