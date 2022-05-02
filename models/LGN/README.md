# LGN

## Requirements

* Python 3.6 or higher
* Pytorch 0.4.1 or higher

## Input Format

BMES tag scheme, with each character its label for one line. Sentences are splited with a null line.

	印   B-LOC
	度   M-LOC
	河   E-LOC
	流   O
	经   O
	印   B-GPE
	度   E-GPE

## Usage

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
		               
## Data

The pretrained character and word embeddings can be downloaded from [Lattice LSTM](https://github.com/jiesutd/LatticeLSTM).
