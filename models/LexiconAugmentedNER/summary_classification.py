
from seqeval.metrics import classification_report
from seqeval.scheme import IOBES
test_dat ='data/DisciplineNER/test.csv'
def read_test(path):
	all_true_tags = []
	temp_sent_tag = []
	with open(path, 'r', encoding='utf-8') as f:
		input_dat = f.readlines()
		f.close()

	for lin in input_dat:
		if len(lin) > 2:
			wd, tag = lin.strip().split(' ')
			temp_sent_tag.append(tag)
		else:
			all_true_tags.append(temp_sent_tag)
			temp_sent_tag = []
	return all_true_tags

def read_pred(pred_path):
	pass

with open('result/transformer_pred_result.txt','r',encoding='utf-8') as f:
	pred= f.read()
	pred=eval(pred)
	f.close()
gold_test = read_test(test_dat)
perf = classification_report(y_true=gold_test,y_pred=pred,digits=4)
print(perf)

# for idx, (t, p) in enumerate(zip(gold_test, pred)):
# 	len_t, len_p = len(t), len(p)
# 	if len_t == len_p:
# 		print(f'idx:{idx}; {len_t}; {len_p}')
# 	else:
# 		print("bug!")
