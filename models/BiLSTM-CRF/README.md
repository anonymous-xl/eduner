<!--
 * @Author       : Li
 * @Date         : 2022-02-17 10:38:30
 * @LastEditTime : 2022-04-21 19:14:25
 * @LastEditors  :  
 * @Description  :  
 * @FilePath     : /EduNER/models/BiLSTM-CRF/README.md
-->
# Named Entity Recognition (NER) using BiLSTM CRF
This is a Pytorch implementation of BiLSTM-CRF for Named Entity Recognition, which is described in [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991)

## Data
Put the EduNER dataset in the data directory.

## Usage
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