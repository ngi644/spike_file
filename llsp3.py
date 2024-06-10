import zipfile
import os

zip_file_path = 'sample/demo.llsp3'
src_folder_file_path = 'sample/demo'
dest_zip_file_path = 'sample/demo2.llsp3'


def open_zip_file(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        
        zip_file.extractall('sample/demo')


def save_zip_file(src_folder_file_path, dest_zip_file_path):
    with zipfile.ZipFile(dest_zip_file_path, 'w', compresslevel=0) as zip_file:
        for file_name in  os.listdir(src_folder_file_path):
            zip_file.write(os.path.join(src_folder_file_path, file_name), file_name)


if __name__ == '__main__':
    
    open_zip_file(zip_file_path)
    # save_zip_file(src_folder_file_path, dest_zip_file_path)