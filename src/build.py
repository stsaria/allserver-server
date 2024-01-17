import subprocess, platform, shutil, os

make_list = ["lang?dir", "config?dir", "README.ja.md?file", "README.ja.html?file"]

os_name = platform.system().lower()

def copy_need_file():
    for i in make_list: 
        if "?dir" in i:
            shutil.copytree(i.split("?")[0], f"bin/{os_name}/"+i.split("?")[0])
        elif "?file" in i:
            shutil.copy(i.split("?")[0], f"bin/{os_name}/"+i.split("?")[0])

def pyinstall():
    os.makedirs(f"bin/{os_name}", exist_ok=True)
    subprocess.run(f"pyinstaller src/allserver.py --onefile --distpath=bin/{os_name}", shell=True)

def install():
    if os.path.isdir("bin"): shutil.rmtree("bin")
    pyinstall()
    copy_need_file()
    shutil.make_archive(f"allserver-{os_name}-bin", 'zip', root_dir=f"./bin/{os_name}")
    shutil.make_archive(f"allserver-{os_name}-bin", 'gztar', root_dir=f"./bin/{os_name}")