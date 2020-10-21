# Derain_OUCD_Net
Official Pytorch Code for "Exploring Overcomplete Representations for Single Image Deraining using CNNs"


[Paper]()

## Prerequisites
- Python >= 3.6  
- [Pytorch](https://pytorch.org/) >= 1.0  
- Torchvision >= 0.2.2  
- Numpy >= 1.14.3

<a href="https://pytorch.org/ "> Pytorch Installation </a>  

### Datasets-Link:

1) [Rain800](https://github.com/hezhangsprinter/ID-CGAN)
2) [JORDER](https://www.icst.pku.edu.cn/struct/Projects/joint_rain_removal.html)
3) [SPANet](https://stevewongv.github.io/derain-project.html)

## Using the Code

### Clone the repository

```bash
git clone https://github.com/jeya-maria-jose/Derain_OUCD_Net
cd Derain_OUCD_Net
```


## Dataset structure

1. Download the rain datasets and arrange the rainy images and clean images in the following order
2. Save the image names into text file (dataset_filename.txt)

```
   .
    ├── data 
    |   ├── train # Training  
    |   |   ├── derain        
    |   |   |   ├── <dataset_name>   
    |   |   |   |   ├── rain              # rain images 
    |   |   |   |   └── norain            # clean images
    |   |   |   └── dataset_filename.txt
    |   └── test  # Testing
    |   |   ├── derain         
    |   |   |   ├── <dataset_name>          
    |   |   |   |   ├── rain              # rain images 
    |   |   |   |   └── norain            # clean images
    |   |   |   └── dataset_filename.txt
```

### Choosing the dataset

Mention the txt file of the dataset in lines 119-121 of train.py, for example
```
    labeled_name = 'DDN_100_split1.txt'
    unlabeled_name = 'real_input_split1.txt'
    val_filename = 'SIRR_test.txt'
``` 
### Training Command 

```bash
python train.py -net OUCD -category indoor -train_batch_size 2 -save_dir rain800_OUCD -num_epochs 200
```
### Testing Command 

Choose the model you want to load from the checkpoint. Change the epoch and bestp variables with the model you need to test. Then, run 

```bash
python test.py -category derain -exp_name DDN_SIRR_withGP

```


