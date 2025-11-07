import PyInstaller.__main__
import os

rmspec = True
if rmspec == True:
    print(".spec file will be removed")
else:
    print(".spec file won't be removed")

print("enter current version(float):")
version = float(input())

PyInstaller.__main__.run([
    'pyterm.py',
    f'--name=pyterm{version}',
    '--onefile',
    '--windowed',
    '--icon=NONE',
    '--add-data=./icon.ico:.',
    '--distpath=output/onefile',
])
if rmspec == True:
    os.remove(f"pyterm{version}.spec")
    print(".spec was removed")
else:
    print(".spec wasnt removed")
print("build end")