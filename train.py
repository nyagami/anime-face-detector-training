import os
import shutil
import subprocess

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

if not os.path.exists('pos.data'):
    raise FileNotFoundError("pos.data not found")
if not os.path.exists('neg'):
    raise FileExistsError("neg dir not found")

run("py get_neg.py")
npos = len(os.listdir('pos'))
nneg = len(os.listdir('neg'))
print(f'{npos} positive images and {nneg} negtive images')

# create vector
print('create .vec file')
if os.path.exists('animeface.vec'):
    os.remove('animeface.vec')
run(f'opencv_apps/createsamples.exe -info pos.data -vec animeface.vec -num {npos} -w 24 -h 24')

# training
if os.path.exists('cascades'):
    shutil.rmtree('cascades')

print('start training...')
run(f'opencv_apps/haartraining.exe -data cascades -vec ./animeface.vec -bg ./neg.txt -numPos {npos} -numNeg {nneg} -w 24 -h 24')
print('remove .vec file')
os.remove('animeface.vec')

# export
if os.path.exists('animeface.xml'):
    os.remove('animeface.xml')
run(f'opencv_apps/haarconv.exe cascades animeface.xml 24 24')
shutil.rmtree('cascades')
print('remove neg.txt')
os.remove('neg.txt')

print('results are stored in animeface.xml')