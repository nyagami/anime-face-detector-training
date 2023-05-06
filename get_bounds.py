import os
from psd_tools import PSDImage

bounded_dir = 'bounded_psds'
pos_dir = 'pos'

pos_data = []

os.makedirs(pos_dir, exist_ok=True)

for idx, psd_file in enumerate(os.listdir(bounded_dir)):
    psd_path = os.path.join(bounded_dir, psd_file)
    psd = PSDImage.open(psd_path)
    img_path = pos_dir + '/' + str(idx).zfill(3) + '.jpg'

    n_obj = 0
    rects = []
    for layer in psd:
        if layer.name == 'Background':
            layer.composite().convert('RGB').convert('L').save(img_path)
        else:
            n_obj += 1
            bbox = layer.bbox
            rects.append(' '.join([str(x) for x in [bbox[0], bbox[1], bbox[2], bbox[3]]]))
    if n_obj:
        pos_data.append((img_path, n_obj, rects))
    else:
        os.remove(img_path)

with open('pos.data', 'w') as f:
    for pos in pos_data:
        f.write('  '.join([pos[0], str(pos[1]), '  '.join(pos[2])]))
        f.write('\n')

