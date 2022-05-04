

# Education-ner-dataset

> EduNER is a first Chinese named entity recognition dataset for education research.

- [Education-ner-dataset](#education-ner-dataset)
  - [EduNER：the full version dataset is coming soon...](#edunerthe-full-version-dataset-is-coming-soon)
  - [Models](#models)
    - [basic description](#basic-description)
    - [tutorial](#tutorial)
  - [Online Annotation Platform](#online-annotation-platform)
  - [Update plan](#update-plan)
  - [Beta application](#beta-application)
  - [License](#license)


## EduNER：the full version dataset is coming soon...

- The related <em>resource paper ✨</em> is under review and a sampled version of the dataset is currently released. After final proofing, the full version of the EduNER dataset will be publicly accessible.
- `sampled_EduNER/` directory contains the sampling version of our dataset.
- `Cohen_Kappa/` directory contains [Cohen's Kappa consistency examination](https://github.com/xuli19/EduNER/tree/main/Cohen_Kappa) description.
- A snapshot of entity types<img src="https://github.com/xuli19/EduNER/blob/main/img/EDUNER_schema.png" alt="EduNER schema" style="zoom:50%;" />

## Models
### basic description

- `models/` directory contains the recent SOTA models.
- LexiconAugementedNER includes SoftLexicon+CNN/Transformer/LSTM models.
- CLNER includes the CL-KL and CL-L<sub>2</sub> models.

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
password: 123
```

- A snapshot of the collaborative corpus labeling platform, the yellow box suggests the candidate entity, and the blue box indicates the corresponding index of entity type. The annotator is asked to identify the correct type index of the candidate entity. The default index of character is set to 0.<img src="https://github.com/xuli19/EduNER/blob/main/img/labeling_platform.jpg" alt="annotation tool" style="zoom:50%;" />

## Update plan

EduNER dataset project is a long-term plan, we expect the dataset to cover more languages and disciplines in higher eduercation. Althgouh this goal is obviously not achieved in a short duration, the dataset will expand to one or two discipline, and will acquire a bigger scale dataset can be used for teaching or learning context. 

- *Pedagogic Psychology, Computer architecture* discipline will be added in the next year (about: 08.2022 ~ 06.2023).
- *Policy, Conference* related corpus will be added in the next phase (about: 08.2022 ~ 01.2023).

## Beta application 

- A beta educational tool ( [EDUNERScore](http://openaied.cn/ents) ) based on our dataset can be accessed. The tool is based on NER technology and allows for analyzing unstructured educational texts in timely manner. Specifically, the tool can extract the discipline entity from a large-scale unstructured texts, e.g., discourse content, online forums, writing documents etc. It will help the stakeholder to better understand the learning or teaching activity. 
- Due to limited computing resources, only cached results can be viewed at current. In addition, only the Chinese version is now available.
- Instruction ![operation](https://github.com/xuli19/EduNER/blob/main/img/sample.gif)

## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
