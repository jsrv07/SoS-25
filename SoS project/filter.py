import os
import shutil

image_dir = 'data/validation/images'
label_dir = 'data/validation/labels'

# Get image base names (without .jpg or .png)
image_ids = [os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]

# Count matched label files
count = 0
for id in image_ids:
    label_file = os.path.join(label_dir, f'{id}.txt')
    if os.path.exists(label_file):
        count += 1
    else:
        print(f'Missing label for: {id}')

print(f'\n✅ Matched images with labels: {count}/{len(image_ids)}')
