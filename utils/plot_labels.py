import os
import random
import numpy as np
import matplotlib.pyplot as plt

def count_labels_in_folder(folder_path):
    label_counts = {str(i): 0 for i in range(10)}
    labels_folder = os.path.join(folder_path, 'labels')

    for filename in os.listdir(labels_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(labels_folder, filename), 'r') as file:
                lines = file.readlines()
                for line in lines:
                    label = line.split()[0]
                    label_counts[label] += 1

    return label_counts

def plot_label_histogram(label_counts, label_name):
    # 对label_counts按照值（count）进行排序
    sorted_counts = {k: v for k, v in sorted(label_counts.items(), key=lambda item: item[1], reverse=True)}
    
    labels = list(sorted_counts.keys())
    counts = list(sorted_counts.values())

    x = np.arange(len(label_name))  # 使用label_name作为x轴
    width = 0.5  # 设置长条的宽度

    fig, ax = plt.subplots()
    colors = [random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k']) for _ in range(len(label_name))]  # 随机选择颜色
    rects = ax.bar(x, counts, width, label='Count', color=colors)  # 设置所有长条的颜色
    
    ax.set_xlabel('Label')
    ax.set_ylabel('Count')
    ax.set_title('Label Counts')
    ax.set_xticks(x)
    ax.set_xticklabels(label_name, rotation=45)  # 旋转45度显示label_name

    # 添加数据标签
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('test.jpg')

# # 统计train文件夹中的label数量
# train_folder = '/datasets/roadpp/train'
# train_label_counts = count_labels_in_folder(train_folder)

# # 统计valid文件夹中的label数量
# valid_folder = '/datasets/roadpp/valid'
# valid_label_counts = count_labels_in_folder(valid_folder)

# # 打印结果
# print('Train Label Counts:', train_label_counts)
# print('Valid Label Counts:', valid_label_counts)

train_label_counts = {'0': 653467, '1': 1970300, '2': 10625, '3': 7223, '4': 2248, '5': 216645, '6': 36193, '7': 30251, '8': 2088, '9': 51649}
valid_label_counts = {'0': 59173, '1': 226749, '2': 1269, '3': 779, '4': 507, '5': 21797, '6': 3696, '7': 3570, '8': 51, '9': 6073}
label_name = ["Ped", "Car", "Cyc", "Mobike", "SmalVeh", "MedVeh", "LarVeh", "Bus", "EmVeh", "TL"]
total_label_counts = {}

for key in train_label_counts.keys():
    total_label_counts[key] = train_label_counts[key] + valid_label_counts[key]


# 绘制直方图
plot_label_histogram(total_label_counts, label_name)

