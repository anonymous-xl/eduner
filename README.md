

# Education-ner-dataset

> EduNER is a Chinese named entity recognition dataset for education research.

```python
├── Models
│   ├── BERT-CRF
│   ├── BERT-NER
│   ├── BiLSTM-CRF
│   ├── CLNER
│   ├── Flat-Lattice-Transformer
│   ├── Flert
│   ├── LEBERT
│   ├── LexiconAugmentedNER
│   ├── LGN
│   ├── LR-CNN
│   ├── MECT4CNER
│   ├── SLK-NER
│   └── TENER
└── sample_EduNER
```

## EduNER

- `models/` directory contains the sampling version of our dataset.
- Quality: [Cohen's Kappa consistency examination](https://github.com/xuli19/EduNER/tree/main/Cohen_Kappa)
- The related <em>resource paper ✨</em> can be found in *Neural Computing & Applications*.
- A snapshot of entity types<img src="https://github.com/xuli19/EduNER/blob/main/img/EDUNER_schema.png" alt="EduNER scheme" style="zoom:50%;" />

- **Reference**
  - Li, X., Wei, C., Jiang, Z. et al. EduNER: a Chinese named entity recognition dataset for education research. Neural Comput & Applic (2023). https://doi.org/10.1007/s00521-023-08635-5


## Models
### basic
- `models/` directory contains the recent SOTA models.
- Lexicon Augemented NER includes SoftLexicon+CNN/Transformer/LSTM models.
- CLNER includes the CL-KL and CL-L<sub>2</sub> models.

### tutorial

- Pre-trained embedding

   We use the Chinese pre-trained character or word embeddings, e.g., [ctb.50d](), [gigaword\_chn.all.a2b.bi.ite50](), and [gigaword\_chn.all.a2b.uni.ite50]() in line with (Yang et al., 2017). We use pre-trained language model, the Chinese BERT:[bert-base-chinese](https://huggingface.co/bert-base-chinese).

- Hyper parameters

  | models                    | epoch | batch size | max length      | learning rate | dropout rate |
  | :------------------------ | :---- | ---------- | :-------------- | :------------ | :----------- |
  | example                   | 100   | 10         | 256             | 0.001         | 0.5          |
  | BiLSTM+CRF                | 100   | 32         | Adaptive length | 0.001         | 0.5          |
  | BERT                      | 20    | 32         | 256             | 5e-5          | 0.5          |
  | BERT+CRF                  | 20    | 16         | 256             | 3e-5          | 0.1          |
  | LR-CNN                    | 150   | 10         | 256             | 1.5e-3        | 0.5          |
  | TENER                     | 100   | 16         | Adaptive length | 7e-4          | 0.15         |
  | LGN                       | 10    | 1          | 256             | 2e-4          | 0.5          |
  | FLAT+BERT                 | 100   | 10         | 200             | 6e-4          | 0.5          |
  | SoftLexicon (CNN)         | 100   | 30         | 256             | 5e-3          | 0.5          |
  | SoftLexicon (Transformer) | 100   | 30         | 256             | 5e-3          | 0.5          |
  | SoftLexicon (LSTM)        | 100   | 30         | 256             | 5e-3          | 0.5          |
  | MECT4CNER                 | 100   | 10         | 200             | 1.4e-3        | 0.2          |
  | SLK-NER                   | 30    | 32         | 256             | 5e-5          | 0.5          |
  | LEBERT                    | 20    | 4          | 256             | 1e-5          | 0.1          |
  | FLERT                     | 10    | 4          | 512             | 5e-6          | 0.1          |
  | CL-KL                     | 10    | 1          | 512             | 5e-6          | 0.1          |
  | CL-L<sub>2</sub>          | 10    | 2          | 512             | 5e-6          | 0.1          |

- Code [instruction](https://github.com/xuli19/EduNER/tree/main/models), reproduce benchmark models

## Online Annotation Platform

- We provide a temporary account to test [the annotation tool](http://openaied.cn/)

```markdown
username: edu
password: 
```

## Update plan

EduNER dataset project is a long-term plan, we expect the dataset to cover more languages and disciplines in higher education. Although this goal is not achieved in a short duration, the dataset will expand to one or two disciplines and will acquire a bigger scale dataset that can be used for teaching or learning contexts.

- *Pedagogic Psychology* discipline will be added in the future.
- *Policy, Conference* related corpus will be added in the future.

## Beta application 

- A beta educational tool ( [EDUNERScore](http://openaied.cn/ents) ) based on our dataset can be accessed. The tool is based on NER technology and allows for the analysis of unstructured educational texts in real-time. Specifically, the tool can extract the discipline entity from large-scale unstructured texts, e.g., discourse content, online forums, writing documents etc. It will help the stakeholder to better understand the learning or teaching activity.
- Due to limited computing resources, only cached results can be viewed at the current. In addition, only the Chinese version is now available.
- Instruction ![operation](https://github.com/xuli19/EduNER/blob/main/img/sample.gif)

## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
