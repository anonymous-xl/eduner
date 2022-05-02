
## Chinese NER using Bert

BERT for Chinese NER. 

### dataset list

1. EduNER: datasets/EduNER


### model list

2. BERT+CRF


### requirement

1. 1.1.0 =< PyTorch < 1.5.0
2. cuda=9.0
3. python3.6+

### input format

Input format (prefer BIO tag scheme), with each character its label for one line. Sentences are splited with a null line.

```text
美	B-LOC
国	I-LOC
的	O
华	B-PER
莱	I-PER
士	I-PER

我	O
跟	O
他	O
```

### run the code

1. Modify the configuration information in `run_ner_crf.py` .
2. `sh scripts/run_ner_crf.sh`

**note**: file structure of the model

```text
├── prev_trained_model
|  └── bert_base
|  |  └── pytorch_model.bin
|  |  └── config.json
|  |  └── vocab.txt
|  |  └── ......
```

