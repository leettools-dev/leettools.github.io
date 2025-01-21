import os
import shutil
import subprocess


def copy_site_content_to_branch_root():
    source_dir = "site/"  # Source directory
    target_branch = "leettools-doc-publish"  # Target branch

    # Check for uncommitted changes and prompt the user to handle them
    status_result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True
    )
    if status_result.stdout:
        print("There are uncommitted changes, please handle them first:")
        print(status_result.stdout)
        return

    # Switch to the target branch
    subprocess.run(["git", "checkout", target_branch], check=True)

    # Get the current working directory, which is the root directory of the target branch
    target_root_dir = os.getcwd()

    # Delete existing content in the target root directory (be careful not to delete important files like .git)
    for item in os.listdir(target_root_dir):
        if item not in [".git", "site"]:  # Keep .git and source site directory
            path = os.path.join(target_root_dir, item)
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    # Copy the contents of the source directory to the root directory, overwriting files with the same name
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(target_root_dir, item)
        if os.path.isdir(s):
            shutil.copytree(
                s, d, dirs_exist_ok=True
            )  # dirs_exist_ok=True allows overwriting existing directories
        else:
            shutil.copy2(s, d)  # copy2 is used to overwrite files

    # Check and delete the site/ folder in the root directory (if it exists)
    site_dir_path = os.path.join(target_root_dir, "site")
    if os.path.exists(site_dir_path):
        shutil.rmtree(site_dir_path)
        print(f"Deleted 'site/' directory from the root of {target_branch} branch.")


if __name__ == "__main__":
    copy_site_content_to_branch_root()
