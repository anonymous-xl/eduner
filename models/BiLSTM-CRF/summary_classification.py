from seqeval.metrics import classification_report
from seqeval.scheme import IOB2

true_sentence = []
pre_sentence = []
with open('result.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
true_tag = []
pred_tag = []
for line in lines:
    if len(line) > 2:
        wd, tg, pg = line.strip().split()
        true_tag.append(tg)
        pred_tag.append(pg)
    else:
        true_sentence.append(true_tag)
        pre_sentence.append(pred_tag)
        true_tag = []
        pred_tag = []

print(f'len true:{len(true_sentence)}, len pred:{len(pre_sentence)}')
print("output performance report...")
report = classification_report(y_pred=pre_sentence, y_true=true_sentence, digits=4, mode='strict', scheme=IOB2)
print(report)
with open('result_report.txt', 'w', encoding='utf-8') as w:
    w.write(str(report))
    w.close()
