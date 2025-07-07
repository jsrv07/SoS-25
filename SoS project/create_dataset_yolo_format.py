import os
import shutil

# 🔹 Source images folder (after downloading images)
DATA_ALL_DIR = 'C:/Users/jayesh/Desktop/New folder/images_downloaded'

# 🔹 Output YOLO dataset folder
DATA_OUT_DIR = os.path.join('.', 'data')

# 🔹 Clean + create output folder structure
for set_ in ['train', 'validation', 'test']:
    for dir_ in [
        os.path.join(DATA_OUT_DIR, set_),
        os.path.join(DATA_OUT_DIR, set_, 'imgs'),
        os.path.join(DATA_OUT_DIR, set_, 'anns')
    ]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.makedirs(dir_, exist_ok=True)  # ✅ replaces os.mkdir

# 🔹 Class to extract (Alpaca)
alpaca_id = '/m/0pcr'

# 🔹 Annotation files
train_csv = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
val_csv = os.path.join('.', 'validation-annotations-bbox.csv')
test_csv = os.path.join('.', 'test-annotations-bbox.csv')

# 🔹 Loop over each split and parse annotations
for j, filename in enumerate([train_csv, val_csv, test_csv]):
    set_name = ['train', 'validation', 'test'][j]
    print(f"Processing: {filename}")

    with open(filename, 'r') as f:
        _ = f.readline()  # skip header
        for line in f:
            try:
                image_id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.strip().split(',')[:13]
            except ValueError:
                continue  # skip malformed lines

            if class_name == alpaca_id:
                # Source and destination image path
                src_img_path = os.path.join(DATA_ALL_DIR, f'{image_id}.jpg')
                dst_img_path = os.path.join(DATA_OUT_DIR, set_name, 'imgs', f'{image_id}.jpg')

                if os.path.exists(src_img_path) and not os.path.exists(dst_img_path):
                    shutil.copy(src_img_path, dst_img_path)

                # Normalized bbox conversion
                x1, x2, y1, y2 = map(float, [x1, x2, y1, y2])
                xc = (x1 + x2) / 2
                yc = (y1 + y2) / 2
                w = x2 - x1
                h = y2 - y1

                label_path = os.path.join(DATA_OUT_DIR, set_name, 'anns', f'{image_id}.txt')
                with open(label_path, 'a') as f_ann:
                    f_ann.write(f'0 {xc} {yc} {w} {h}\n')
