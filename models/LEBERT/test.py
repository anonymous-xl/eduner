from seqeval.metrics import classification_report

with open("data/result/NER/edu/lebertcrf/WCBertCRF_Token-Test-42100.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split('\t')
    # print(data)

data = data[:-1]

y_true = []
y_pred = []
sentence_true = []
sentence_pred = []
for i in range(len(data)):
    line = data[i]
    if len(line) >= 3:
        sentence_true.append(line[1])
        sentence_pred.append(line[2])
    else:
        y_true.append(sentence_true)
        y_pred.append(sentence_pred)
        sentence_true = []
        sentence_pred = []

classification_report_res = classification_report(y_pred=y_pred, y_true=y_true, digits=4)
print(classification_report_res)
with open('classification_report1120.txt', 'w', encoding='utf-8') as w:
    w.write(classification_report_res)
    w.close()
print('成功输出classification报告！')