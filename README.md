<div align="center">

<h1>Bilevel Layer-Positioning LoRA for Real Image Dehazing</h1>

<div>
    <strong>Yan Zhang</a>&emsp;
    <strong>Long Ma</a>&emsp;
    <strong>Yuxin Feng</a>&emsp;
    <strong>Zhe Huang</a>&emsp;
    <strong>Fan Zhou</a>&emsp;
    <strong>Zhuo Su</a>
</div>

<div>
    :star: <strong>Accepted to CVPR 2026 :star:
</div>

<div>
    <h4 align="center">
        <a href="https://arxiv.org/abs/2603.10872" target='_blank'>[arXiv]</a> •
        <a href="https://drive.google.com/drive/folders/1qEmYEONhX8e0b7PLikKxMCKNu_j7pu6b?usp=sharing" target='_blank'>[GoogleDrive Weight]</a> •
        <a href="https://pan.baidu.com/s/1uFnB4ov9hiNSnRE8lFMdXw?pwd=0519" target='_blank'>[BaiduNetdisk Weight]</a> 
    </h4>
</div>

</div>

## :mega: Updates
- **2026.03.10**: :fire::fire::fire: Training codes, and initial checkpoints are publicly available now.
- **2026.02.21**: :tada::tada::tada: Accepted by ***CVPR 2026***.


## :mag: Performance Comparison

<img src="fig/FirstFigure.jpg" alt="Model" style="zoom:80%;" />

## :pencil2: Results

<img src="fig/Comparisons1.jpg" alt="Results" style="zoom:80%;" />
<img src="fig/Comparisons3.jpg" alt="Results" style="zoom:80%;" />

## :desktop_computer: Environment

Step 1. Clone this repo:

```
git clone https://github.com/YanZhang-zy/BiLaLoRA.git
cd BiLaLoRA/
```

Step 2. Create a new conda environment and install dependencies:

```
conda create -n BiLaLoRA python=3.10
conda activate BiLaLoRA
conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install -r requirements.txt
```

##  :book: Data Preparation

Step 1. Download the haze dataset from websites or papers.

Step 2. Make sure the file structure is consistent with the following:
```
dataset/
├── Synthetic_Data
│   ├── test
│   |   ├── clear
│   |   └── hazy
│   └── train
│       ├── clear
│       └── hazy
└── Real_Data
```

The datasets can be downloaded at
+ [Reside](https://sites.google.com/view/reside-dehaze-datasets/reside-v0)
+ [Haze4K](https://pan.baidu.com/s/19stkJ3aaF8WgHK2FBytnZA?pwd=0411)
+ [RIDCP](https://github.com/RQ-Wu/RIDCP_dehazing)
+ [Real_Data](https://pan.baidu.com/s/1GS9qkwcBcKB411pdSwFcDg?pwd=0519)


## :hotsprings: Model Training
Step 1. Download the clip model weight from [[BaiduPan](https://pan.baidu.com/s/1wrGspYjjIH3sC7yuQUfMjg?pwd=0519)].

Step 2. Make sure the file structure is consistent with the following:
```
clip_model/
├── RN101.pt
└── ViT-B-32.pt
```

Step 3. Run the following script to train BiLaLoRA from scratch:
```
python Base_Train.py
python Reparam.py
python BiLaLoRA_Train.py
python BiLaLoRA_Eval.py
```

## :taxi: Model Testing
Step 1. Download the pre-trained weights from [[BaiduPan](https://pan.baidu.com/s/19wIc2s1O_o1F4YMchF_7sg?pwd=0519)].

Step 2. Make sure the file structure is consistent with the following:
```
weight/
├── Base.pth
└── LoRA.pth
```

Step 3. Run the following script to test BiLaLoRA:
```
python BiLaLoRA_Test.py
```

## :clipboard: Acknowledgments
We would like to extend our gratitude to the following implementations for their contributions to the development of BiLaLoRA:
- [DEA-Net](https://github.com/cecret3350/DEA-Net.git) for providing the re-parameterization technique.

## :triangular_flag_on_post: Citation
If you find our paper and repo are helpful for your research, please consider citing:

```bibtex
@inproceedings{BiLaLoRA,
  title={Bilevel Layer-Positioning LoRA for Real Image Dehazing},
  author={Yan Zhang, Long Ma, Yuxin Feng, Zhe Huang, Fan Zhou, Zhuo Su},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={1-10},
  year={2026}
}
```

## :mailbox_with_mail: Contacts 
If you have any questions or suggestions about this repo, please feel free to contact me (zhangy2779@mail2.sysu.edu.cn).
