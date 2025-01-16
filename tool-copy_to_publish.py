import shutil
import subprocess
import os

def copy_site_content_to_branch_root():
    source_dir = 'site/'  # 源目录
    target_branch = 'leettools-doc-publish'  # 目标分支

    # 检查是否有未提交的更改，并提示用户处理
    status_result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if status_result.stdout:
        print("有未提交的更改，请先处理这些更改:")
        print(status_result.stdout)
        return

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

    # 检查并删除根目录中的 site/ 文件夹（如果存在）
    site_dir_path = os.path.join(target_root_dir, 'site')
    if os.path.exists(site_dir_path):
        shutil.rmtree(site_dir_path)
        print(f"Deleted 'site/' directory from the root of {target_branch} branch.")


if __name__ == "__main__":
    copy_site_content_to_branch_root()