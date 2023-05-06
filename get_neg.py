import os

neg_dir = 'neg'

with open('neg.txt', 'w') as f:
    for file in os.listdir(neg_dir):
        img_path = neg_dir + '/' + file
        f.write(img_path)
        f.write('\n')
