import argparse
import json
import os
import torch

parser = argparse.ArgumentParser()

parser.add_argument('--device', type=str, default='Automatic detection')
parser.add_argument('--epochs', type=int, default=30)
parser.add_argument('--iters_per_epoch', type=int, default=200)
parser.add_argument('--finer_eval_step', type=int, default=100000)
parser.add_argument('--start_lr', default=0.00002, type=float, help='start learning rate')
parser.add_argument('--end_lr', default=0.00002, type=float, help='end learning rate')
parser.add_argument('--no_lr_sche', action='store_true', help='no lr cos schedule')
parser.add_argument('--momentum', default=0.9)
parser.add_argument('--w_momentum', default=0.9)
parser.add_argument('--weight_decay', default=3e-4)
parser.add_argument('--w_weight_decay', default=3e-4)
parser.add_argument('--eps', default=1e-08)
parser.add_argument('--betas', default=(0.9, 0.999))
parser.add_argument('--top_k_lora', default=3)
parser.add_argument('--lora_r', default=8)
parser.add_argument('--lora_alpha', default=16)
parser.add_argument('--verbose_params', default=False)

parser.add_argument('--w_loss_H2C', default=1, type=float, help='weight of H2C loss')

parser.add_argument('--exp_dir', type=str, default='./experiment')
parser.add_argument('--model_name', type=str, default='BiLaLoRA')
parser.add_argument('--saved_model_dir', type=str, default='saved_model')
parser.add_argument('--saved_data_dir', type=str, default='saved_data')
parser.add_argument('--dataset', type=str, default='DEA')

opt = parser.parse_args()
opt.device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 构建目录结构
dataset_dir = os.path.join(opt.exp_dir, opt.dataset)
model_dir = os.path.join(dataset_dir, opt.model_name)

# 更新为完整路径
opt.saved_model_dir = os.path.join(model_dir, opt.saved_model_dir)
opt.saved_data_dir = os.path.join(model_dir, opt.saved_data_dir)

