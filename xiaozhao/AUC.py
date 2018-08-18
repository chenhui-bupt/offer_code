
def naive_auc(preds, labels):
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pairs = n_pos * n_neg
    accumulated_neg = 0
    satisfied_pair = 0
    preds_labels = zip(preds, labels)
    preds_labels = sorted(preds_labels, key=lambda x: x[0])  #升序
    for i in range(len(labels)):
        if preds_labels[i][1] == 1:
            satisfied_pair += accumulated_neg  # 该正例样本有多少个负例样本的score小于他，满足
        else:
            accumulated_neg += 1
    return satisfied_pair/total_pairs

def approximate_auc(preds, labels, bins=100):
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pairs = n_pos * n_neg
    accumulated_neg = 0
    satisfied_pair = 0
    pos = [0] * bins
    neg = [0] * bins
    width = 1.0/bins
    for i in range(len(labels)):  # 按概率值score等位分箱，做频率直方图
        bin = int(preds[i]/width)
        if labels[i] == 1:
            pos[bin] += 1
        else:
            neg[bin] += 1

    for i in range(bins):
        satisfied_pair += pos[i] * accumulated_neg + 0.5 * pos[i] * neg[i]  # (n1 + 0.5 * n2)/n
        accumulated_neg += neg[i]
    return satisfied_pair/total_pairs

import numpy as np
import random
random.seed(22)
preds = [random.random() for i in range(1000)]
labels = [random.randint(0, 1) for i in range(1000)]
print(naive_auc(preds, labels))
print(approximate_auc(preds, labels))




