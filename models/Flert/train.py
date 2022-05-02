from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TransformerWordEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

columns = {0: 'text', 1: 'ner'}

data_folder = '/home/lixu/baseline_ners/Flert/datasets/EduNER'

corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.csv',
                              test_file='test.csv',
                              dev_file='dev.csv')

label_type = 'ner'

label_dict = corpus.make_label_dictionary(label_type=label_type)

embeddings = TransformerWordEmbeddings(model='xlm-roberta-large',
                                       layers="-1",
                                       subtoken_pooling="first",
                                       fine_tune=True,
                                       use_context=True,
                                       )

tagger = SequenceTagger(hidden_size=256,
                        embeddings=embeddings,
                        tag_dictionary=label_dict,
                        tag_type='ner',
                        use_crf=False,
                        use_rnn=False,
                        reproject_embeddings=False,
                        )

trainer = ModelTrainer(tagger, corpus)

trainer.fine_tune('resources/taggers/sota-ner-flert',
                  learning_rate=5.0e-6,
                  mini_batch_size=4,
                  mini_batch_chunk_size=1,  # remove this parameter to speed up computation if you have a big GPU
                  )