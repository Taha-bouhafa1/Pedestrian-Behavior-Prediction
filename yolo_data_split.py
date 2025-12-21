import os
import random
import shutil

ROOT = "jaad_yolo"
IMG_SRC = os.path.join(ROOT, "images")
LBL_SRC = os.path.join(ROOT, "labels")

IMG_TRAIN = os.path.join(ROOT, "images/train")
IMG_VAL = os.path.join(ROOT, "images/val")
LBL_TRAIN = os.path.join(ROOT, "labels/train")
LBL_VAL = os.path.join(ROOT, "labels/val")

os.makedirs(IMG_TRAIN, exist_ok=True)
os.makedirs(IMG_VAL, exist_ok=True)
os.makedirs(LBL_TRAIN, exist_ok=True)
os.makedirs(LBL_VAL, exist_ok=True)

images = [f for f in os.listdir(IMG_SRC) if f.endswith(".png")]

random.shuffle(images)
split_idx = int(0.8 * len(images))

train_imgs = images[:split_idx]
val_imgs = images[split_idx:]

def move(img_list, img_dst, lbl_dst):
    for img in img_list:
        base = img.replace(".png", "")
        lbl = base + ".txt"

        shutil.move(
            os.path.join(IMG_SRC, img),
            os.path.join(img_dst, img)
        )

        shutil.move(
            os.path.join(LBL_SRC, lbl),
            os.path.join(lbl_dst, lbl)
        )

move(train_imgs, IMG_TRAIN, LBL_TRAIN)
move(val_imgs, IMG_VAL, LBL_VAL)

print("Dataset split completed")
print(f"Train images: {len(train_imgs)}")
print(f"Val images: {len(val_imgs)}")
