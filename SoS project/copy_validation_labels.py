import os
import shutil

val_img_dir = "data/validation/images"
train_label_dir = "data/train/labels"
val_label_dir = "data/validation/labels"

val_ids = [os.path.splitext(f)[0] for f in os.listdir(val_img_dir) if f.endswith(('.jpg', '.png'))]

copied = 0
missing = []

for vid in val_ids:
    src = os.path.join(train_label_dir, f"{vid}.txt")
    dst = os.path.join(val_label_dir, f"{vid}.txt")
    if os.path.exists(src):
        shutil.copy(src, dst)
        copied += 1
    else:
        missing.append(vid)

print(f"\n✅ Copied: {copied}/{len(val_ids)}")
if missing:
    print("❌ Missing labels for:")
    for m in missing:
        print(m)
