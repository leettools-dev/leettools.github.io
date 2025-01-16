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

    # 复制文件夹内容到根目录，直接覆盖同名文件
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(target_root_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)  # dirs_exist_ok=True 允许覆盖已存在的目录
        else:
            shutil.copy2(s, d)  # copy2 用于覆盖文件

    # 添加更改到 git
    subprocess.run(['git', 'add', '.'], check=True)

    # 提交更改
    subprocess.run(['git', 'commit', '-m', 'Update root content from site directory'], check=True)

    # 可选：推送到远程仓库
    # subprocess.run(['git', 'push'], check=True)

    # 切换回原始分支（如果需要）
    # subprocess.run(['git', 'checkout', '-'], check=True)

if __name__ == "__main__":
    copy_site_content_to_branch_root()