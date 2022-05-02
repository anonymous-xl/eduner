from seqeval.metrics import classification_report


def read_bio(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
        f.close()
    sentences = []
    gold_labels = []
    sent = []
    labels = []
    for line in all_lines:
        if len(line) > 2:
            # print(line)
            wd, label = line.strip().split()
            sent.append(wd)
            labels.append(label)
        else:
            sentences.append(sent)
            gold_labels.append(labels)
            sent = []
            labels = []
    return sentences, gold_labels


gold_path = 'data/DisciplineNERBMES/test.csv'
pred_path = 'data/DisciplineNERBMES/results.txt'

_, gold_res = read_bio(gold_path)
_, pred_res = read_bio(pred_path)

class_res = classification_report(y_true=gold_res, y_pred=pred_res, digits=4)

with open('data/DisciplineNERBMES/classification_result.txt', 'w', encoding='utf-8') as w:
    w.write(class_res)
    w.close()
