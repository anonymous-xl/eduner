from seqeval.metrics import classification_report
import json
from seqeval.scheme import IOB1, IOB2

json_file = 'outputs/resume_output/bert/test_prediction.json'
with open(json_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
results = []
for line in lines:
    new_line = json.loads(line)
    pred = new_line['tag_seq']
    temp_pred = pred.strip().split(' ')
    # print(temp_pred)
    results.append(temp_pred)

all_true_tags = []
temp_sent_tag = []
with open('datasets/resume/test.char.bmes', 'r', encoding='utf-8') as f:
    input_dat = f.readlines()
    f.close()

for lin in input_dat:
    if len(lin) > 2:
        wd, tag = lin.strip().split(' ')
        temp_sent_tag.append(tag)
    else:
        all_true_tags.append(temp_sent_tag)
        temp_sent_tag = []

print(f'pred:{len(results)}, tru:{len(all_true_tags)}')

#==================== 评估句子长度为128的weibo数据集 ====================#
# 如果裁剪了句子长度，需要特殊处理，要不然序列长度的不一致无法评估performance.
# new_true = [x if len(x) <128 else x[:126] for x in all_true_tags]
# print([len(x) for x in new_true])
# performance = classification_report(y_true=all_true_tags, y_pred=results, digits=4)
# print(performance)

#==================== 评估其它句子长度的数据集 ====================#
performance = classification_report(y_true=all_true_tags, y_pred=results, digits=4)
print(performance)