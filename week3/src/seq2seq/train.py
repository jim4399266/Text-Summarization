# -*- coding:utf-8 -*-
# Created by LuoJie at 11/29/19
import sys
import os
from pathlib import Path

# root = Path(os.path.abspath(__file__)).parent.parent.parent
# sys.path.append(root)
import torch

from src.seq2seq.seq2seq_model import Seq2Seq
from src.seq2seq.train_helper import train_model
# from src.utils.gpu_utils import config_gpu
from src.utils.params_utils import get_params
from src.utils.wv_loader import Vocab


def train(params):
    # GPU资源配置
    # config_gpu()
    device = torch.device('cuda:0' if torch.cuda.is_available() and params['device']=='cuda' else 'cpu')
    params['device'] = device
    # 读取vocab训练
    vocab = Vocab(params["vocab_path"], params["vocab_size"])

    params['vocab_size'] = vocab.count

    # 构建模型
    print("Building the model ...")
    model = Seq2Seq(params, vocab).to(device)

    # 获取保存管理者
    # checkpoint = tf.train.Checkpoint(Seq2Seq=model)
    # checkpoint_manager = tf.train.CheckpointManager(checkpoint, params['checkpoint_dir'], max_to_keep=5)

    # 训练模型
    train_model(model, vocab, params, device)


if __name__ == '__main__':
    # 获得参数
    params = get_params()
    params['mode'] = 'train'
    # 训练模型
    train(params)
