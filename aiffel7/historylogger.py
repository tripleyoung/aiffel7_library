# 기여자: 윤여원
# 기여 날짜: [2024-01-02]
# 설명: 에폭이 끝날때 히스토리 관련 로그를 만들어준다.

import os
import json
from tensorflow.keras.callbacks import Callback
import matplotlib.pyplot as plt


class HistoryLogger(Callback):
    def __init__(self, log_file):
        self.log_file = log_file
        self.history = {}

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        
        # 이전 로그 파일 읽기 (존재하면)
        previous_history = {}
        if os.path.isfile(self.log_file):
            with open(self.log_file, 'r') as f:
                previous_history = json.load(f)
        
        # 이전 에폭 값 가져오기
        previous_epochs = previous_history.get('epoch', [])
        if previous_epochs:
            last_epoch = previous_epochs[-1] + 1  # 마지막 에폭 값 + 1
        else:
            last_epoch = 0  # 이전 로그가 없으면 0부터 시작
        
        # 현재 에폭 번호 설정
        current_epoch = last_epoch + epoch
        
        # 현재 에폭 번호와 메트릭 저장
        self.history.setdefault('epoch', []).append(current_epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)

        # 로그 파일에 현재까지의 히스토리 저장
        with open(self.log_file, 'w') as f:
            json.dump(self.history, f)
def history_graph(history):
    # 손실 그래프 그리기
    plt.figure(figsize=(8, 4))
    plt.plot(history['epoch'], history['loss'], label='Training Loss')
    plt.plot(history['epoch'], history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    # 정확도 그래프 그리기
    plt.figure(figsize=(8, 4))
    plt.plot(history['epoch'], history['accuracy'], label='Training Accuracy')
    plt.plot(history['epoch'], history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
