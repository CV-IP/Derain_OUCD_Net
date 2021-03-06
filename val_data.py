
import torch.utils.data as data
from PIL import Image
from torchvision.transforms import Compose, ToTensor, Normalize
import numpy as np
from random import randrange


# --- Validation/test dataset --- #
class ValData(data.Dataset):
    def __init__(self, val_data_dir):
        super().__init__()
        val_list = val_data_dir + 'val_list_rain800.txt'
        with open(val_list) as f:
            contents = f.readlines()
            haze_names = [i.strip() for i in contents]
            gt_names = [i.strip().replace('rain','norain') for i in haze_names]

        self.haze_names = haze_names
        self.gt_names = gt_names
        self.val_data_dir = val_data_dir

    def get_images(self, index):
        haze_name = self.haze_names[index]
        gt_name = self.gt_names[index]
        haze_img = Image.open(self.val_data_dir + haze_name)
        gt_img = Image.open(self.val_data_dir  + gt_name)

        wd_new = 256#int(16*np.ceil(haze_img.size[0]/16.0))
        ht_new = 256#int(16*np.ceil(haze_img.size[1]/16.0))
        if ht_new>512:
            ht_new = 512
        if wd_new>512:
            wd_new = 512
        

        haze_img = haze_img.resize((wd_new,ht_new), Image.ANTIALIAS)
        gt_img = gt_img.resize((wd_new, ht_new), Image.ANTIALIAS)
        width, height = haze_img.size
        crop_width = 128
        crop_height = 128
        # x, y = randrange(0, width - crop_width + 1), randrange(0, height - crop_height + 1)
        # haze_crop_img = haze_img.crop((x, y, x + crop_width, y + crop_height))
        # gt_crop_img = gt_img.crop((x, y, x + crop_width, y + crop_height))

        # --- Transform to tensor --- #
        transform_haze = Compose([ToTensor(), Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        transform_gt = Compose([ToTensor()])
        haze = transform_haze(haze_img)
        gt = transform_gt(gt_img)

        return haze, gt, haze_name

    def __getitem__(self, index):
        res = self.get_images(index)
        return res

    def __len__(self):
        return len(self.haze_names)
