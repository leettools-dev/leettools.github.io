import shutil
import subprocess
import os

def copy_site_content_to_branch_root():
    source_dir = 'site/'  # 源目录
    target_branch = 'leettools-doc-publish'  # 目标分支

    # 切换到目标分支
    subprocess.run(['git', 'checkout', target_branch], check=True)

    # 获取当前工作目录，即目标分支的根目录
    target_root_dir = os.getcwd()

    # 删除目标根目录现有内容（慎重操作，确保不会删除.git等重要文件）
    for item in os.listdir(target_root_dir):
        if item not in ['.git', 'site']:  # 保留.git和源site目录
            path = os.path.join(target_root_dir, item)
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    # 复制文件夹内容到根目录，直接覆盖同名文件
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(target_root_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)  # dirs_exist_ok=True 允许覆盖已存在的目录
        else:
            shutil.copy2(s, d)  # copy2 用于覆盖文件


if __name__ == "__main__":
    copy_site_content_to_branch_root()