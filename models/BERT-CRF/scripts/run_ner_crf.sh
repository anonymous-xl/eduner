# CURRENT_DIR='/home/***/baseline_ner/BERT-NER-Pytorch/'
BERT_BASE_DIR='prev_trained_model/bert-base-chinese'
DATA_DIR='datasets'
OUTPUR_DIR='outputs'
# TASK_NAME="weibo"
TASK_NAME='resume'
# TASK_NAME='weibo'
#
  # --do_train \
  # --do_eval \

# resume 数据集是bioes标注
python run_ner_crf.py \
  --markup='bios' \
  --model_type=bert \
  --model_name_or_path=$BERT_BASE_DIR \
  --task_name=$TASK_NAME \
  --do_predict \
  --do_lower_case \
  --data_dir=$DATA_DIR/${TASK_NAME}/ \
  --train_max_seq_length=256 \
  --eval_max_seq_length=256 \
  --per_gpu_train_batch_size=16 \
  --per_gpu_eval_batch_size=16 \
  --learning_rate=3e-5 \
  --crf_learning_rate=1e-3 \
  --num_train_epochs=20 \
  --logging_steps=-1 \
  --save_steps=-1 \
  --output_dir=$OUTPUR_DIR/${TASK_NAME}_output/ \
  --overwrite_output_dir \
  --seed=20211231
