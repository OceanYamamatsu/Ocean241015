import os
from google.colab import drive

# 不要なパッケージを削除（wandbなし）
!pip uninstall -y wandb

# ===  Google Drive をマウント ===
drive.mount('/content/drive')

# WebUIのインストール
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git /content/stable-diffusion-webui

# === 自分の環境に合わせて修正する  ===
LOCAL_MODEL_PATH = "/content/drive/MyDrive/SDGS/sd/Pony/checkpoint/autismmixSDXL_autismmixConfetti.safetensors"
 # モデルのパス（正しく変更する）
LOCAL_LORA_DIR = "/content/drive/MyDrive/SDGS/sd/Pony/Lora"
 #  LoRA フォルダのパス（正しく変更する）

# === WebUI のフォルダ設定 ===
MODEL_DIR = "/content/stable-diffusion-webui/models/Stable-diffusion"
LORA_DIR = "/content/stable-diffusion-webui/models/Lora"

# フォルダを作成（すでにある場合はスキップ）
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LORA_DIR, exist_ok=True)

# ===  モデルを WebUI にコピー（上書きはしない） ===
if os.path.exists(LOCAL_MODEL_PATH):
    os.system(f'cp -n "{LOCAL_MODEL_PATH}" "{MODEL_DIR}/model.safetensors"')
else:
    print(f" エラー: モデルファイルが無い！ {LOCAL_MODEL_PATH} を確認してください")

# ===  LoRA を WebUI にコピー（フォルダごとコピー） ===
if os.path.exists(LOCAL_LORA_DIR):
    os.system(f'cp -rn "{LOCAL_LORA_DIR}"* "{LORA_DIR}/"')
else:
    print(f" 注意: LoRA フォルダが無い！スキップした")

# ===  WebUI を起動（初期設定によるHugging Face からの勝手なダウンロードを防ぐ） ===
# Web UIの起動
%cd /content/stable-diffusion-webui
!python launch.py --share --no-half-vae --enable-insecure-extension-access --gradio-queue --skip-torch-cuda-test --no-download