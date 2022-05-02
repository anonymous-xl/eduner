# Model

## Flat + BERT

**Requirement**

```bash
Python: 3.7.3
PyTorch: 1.2.0
FastNLP: 0.5.0
Numpy: 1.16.4
```

**Run**

```
cd Flat-Lattice-Transformer
```

1. Download the character embeddings and word embeddings.

   Character and Bigram embeddings (gigaword_chn.all.a2b.{'uni' or 'bi'}.ite50.vec) : [Google Drive](https://drive.google.com/file/d/1_Zlf0OAZKVdydk7loUpkzD2KPEotUE8u/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

   Word(Lattice) embeddings:

   yj, (ctb.50d.vec) : [Google Drive](https://drive.google.com/file/d/1K_lG3FlXTgOOf8aQ4brR9g3R40qi1Chv/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

   ls, (sgns.merge.word.bz2) : [Baidu Pan](https://pan.baidu.com/s/1luy-GlTdqqvJ3j-A4FcIOw)

2. Modify the `paths.py` to add the pretrained embedding and the dataset

3. Run following commands

   ```bash
   python preprocess.py
   cd V1
   python flat_main.py --dataset edu
   ```

## MECT4CNER

**Requirement**

```bash
torch==1.5.1
numpy==1.18.5
FastNLP==0.5.0
fitlog==0.3.2
```

**Run**

```
cd MECT4CNER
```

1. Download the pretrained character embeddings and word embeddings and put them in the data folder.

   - Character embeddings (gigaword_chn.all.a2b.uni.ite50.vec): [Google Drive](https://drive.google.com/file/d/1_Zlf0OAZKVdydk7loUpkzD2KPEotUE8u/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
   - Bi-gram embeddings (gigaword_chn.all.a2b.bi.ite50.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
   - Word(Lattice) embeddings (ctb.50d.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

2. Modify the `Utils/paths.py` to add the pretrained embedding and the dataset

3. Run following commands

   ```bash
   python Utils/preprocess.py
   python main.py --dataset edu
   ```

## SLK-NER

**Requirement**

```bash
python == 3.6.10 
torch == 1.3.1 
numpy == 1.17.4 
seqeval == 0.0.12 
tqdm == 4.40.0 
```

**Run**

```bash
cd SLK-NER
```

1. Download the character embeddings and word embeddings.

   Character embeddings: [chinese_L-12_H-768_A-12](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)
   Word embeddings: [ctb.50d.vec](https://drive.google.com/file/d/1K_lG3FlXTgOOf8aQ4brR9g3R40qi1Chv/view?usp=sharing)

2. Modify DATA_DIR and OUTPUT_DIR in `run_ner.sh`

3. Run the following commands

   ```bash
   bash run_ner.sh
   ```

## LEBERT

**Requirement**

```bash
Python 3.7.0
Transformer 3.4.0
Numpy 1.18.5
Packaging 17.1
skicit-learn 0.23.2
torch 1.6.0
tqdm 4.50.2
multiprocess 0.70.10
tensorflow 2.3.1
tensorboardX 2.1
seqeval 1.2.1
```

**Run**

```
cd LEBERT
```

1. Copy EduNER dataset to `data/NER/`
2. Convert .char.bmes file to .json file, `python to_json.py`
3. run the shell, `bash run_edu.sh`

## FLERT

**Requirement**

PyTorch 1.5+ and Python 3.6+

Install [flair](https://github.com/flairNLP/flair)

**Run**

```bash
cd Flert
# revise data_folder in train.py
python train.py
```

## CLNER

**Requirement**

```bash
python==3.6
gensim==3.8.1
h5py==2.8.0
PyYAML==5.2
scikit-learn==0.24.2
scipy==1.5.4
torch==1.4.0
tqdm==4.62.3
transformers==3.0.0
```

**Run**

```bash
cd CLNER
```

1. Revise data_folder in `config/eduner_doc_cl_kl.yaml` and `config/eduner_doc_cl_l2.yaml`

2. Run:

   ```bash
   CUDA_VISIBLE_DEVICES=0 python train.py --config config/eduner_doc_cl_kl.yaml
   CUDA_VISIBLE_DEVICES=0 python train.py --config config/eduner_doc_cl_l2.yaml
   ```

   



## BiLSTM+CRF
**Data**
Put the EduNER dataset in the data directory.

**Run**
For training the model, you can use the following command:
```
sh run.sh train
```
For those who are not able to use GPU, use the following command to train:
```
sh run.sh train-without-cuda
```
For testing, you can use the following command:
```
sh run.sh test
```
Also, if you have no GPU, you can use the following command(this procedure won't take long time when using CPU):
```
sh run.sh test-without-cuda
```

If you want to change some hyper-parameters, use the following command to refer to the options.
```
python run.py --help
```

## BERT-CRF

**Data**
1. EduNER: datasets/EduNER


**model** 

2. BERT+CRF


**requirement**

1. 1.1.0 =< PyTorch < 1.5.0
2. cuda=9.0
3. python3.6+


**input format**

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

**run the code**

1. Modify the configuration information in `run_ner_crf.py` .
2. `sh scripts/run_ner_crf.sh`



## BERT NER

**Requirements**

-  `python3`
- `pip3 install -r requirements.txt`

**Run**

`python run_ner.py --data_dir=data/ --bert_model=/data2/lx/bert-base-chinese --task_name=ner --output_dir=out_base --max_seq_length=256 --do_train --num_train_epochs 10 --do_eval --eval_on test --warmup_proportion=0.1`

## LexiconAugmentedNER

**Requirement**:
Python 3.6
Pytorch 0.4.1

**Input format:**
CoNLL format, with each character and its label split by a whitespace in a line. The "BMES" tag scheme is prefered.

别 O 

错 O

过 O

邻 O

近 O

大 B-LOC

鹏 M-LOC

湾 E-LOC

的 O

湿 O

地 O

**Pretrain embedding:**
The pretrained embeddings(word embedding, char embedding and bichar embedding) are the same with [Lattice LSTM](https://www.aclweb.org/anthology/P18-1144)

**Run the code:**
1. Download the character embeddings and word embeddings from [Lattice LSTM](https://github.com/jiesutd/LatticeLSTM) and put them in the `data` folder.
2. Put the four datasets in `data/EduNER`.


- To train on EduNER:

`python main.py --status train --train data/EduNER/train.char.bmes --dev data/EduNER/dev.char.bmes --test data/EduNER/test.char.bmes --modelname disner14 --savedset data/EduNER/dis14.dset`

4. To train/test your own data: modify the command with your file path and run.


## LGN

**Requirements**

* Python 3.6 or higher
* Pytorch 0.4.1 or higher

**Input Format**

BMES tag scheme, with each character its label for one line. Sentences are splited with a null line.

	印   B-LOC
	度   M-LOC
	河   E-LOC
	流   O
	经   O
	印   B-GPE
	度   E-GPE

**Usage**

* Training

		python main.py --status train \
		               --train data/EduNER/train.char.bmes \
		               --dev data/EduNER/dev.char.bmes \
		               --test data/EduNER/test.char.bmes \
		               --saved_model saved_model/model_onto4ner \
		               --saved_set data/EduNER/saved.dset
		               
* Testing

		python main.py --status test \
		               --test data/EduNER/test.char.bmes \
		               --saved_model saved_model/model_onto4ner \
		               --saved_set data/EduNER/saved.dset
		               
* Decoding (Raw file can either be labeled or not.)

		python main.py --status decode \
		               --raw data/EduNER/test.char.bmes \
		               --output tagged_file.txt \
		               --saved_model saved_model/model_onto4ner \
		               --saved_set data/EduNER/saved.dset
		               
**Data**

The pretrained character and word embeddings can be downloaded from [Lattice LSTM](https://github.com/jiesutd/LatticeLSTM).
















## LR-CNN

**Requirement**:

Python 3.6
Pytorch 0.4.1  

**Input format:**

CoNLL format, with each character and its label splited by a whitespace in a line. The "BMES" tag scheme is prefered.

	别 O  
	错 O  
	过 O  
	邻 O  
	近 O  
	大 B-LOC  
	鹏 M-LOC  
	湾 E-LOC  
	的 O  
	湿 O  
	地 O  

** Pretrain embedding:**

The pretrained embeddings(word embedding, char embedding) are the same with Lattice LSTM(https://github.com/jiesutd/LatticeLSTM)  

**Run the code:**

1. Download the character embeddings and word embeddings and put them in the `data` folder.
2. To train/test the demo: `sh train.sh` / `sh test.sh`
3. To train/test your own data: modify the 'train.sh' or 'test.sh' file with your file path, and run the shell file.