import os
from google.colab import drive

# === ✅ Google Drive をマウント ===
drive.mount('/content/drive')

# === ❗❗ あなたの環境に合わせて修正してください ❗❗ ===
LOCAL_MODEL_PATH = "/content/drive/MyDrive/sd_model/model.safetensors"  # ✅ モデルのパス（正しく変更する）
LOCAL_LORA_DIR = "/content/drive/MyDrive/sd_model/lora/"  # ✅ LoRA フォルダのパス（正しく変更する）

# === WebUI のフォルダ設定 ===
MODEL_DIR = "/content/stable-diffusion-webui/models/Stable-diffusion"
LORA_DIR = "/content/stable-diffusion-webui/models/Lora"

# フォルダを作成（すでにある場合はスキップ）
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LORA_DIR, exist_ok=True)

# === ✅ モデルを WebUI にコピー（上書きしない） ===
if os.path.exists(LOCAL_MODEL_PATH):
    os.system(f'cp -n "{LOCAL_MODEL_PATH}" "{MODEL_DIR}/model.safetensors"')
else:
    print(f"🚨 エラー: モデルファイルが見つかりません！ {LOCAL_MODEL_PATH} を確認してください")

# === ✅ LoRA を WebUI にコピー（フォルダごとコピー） ===
if os.path.exists(LOCAL_LORA_DIR):
    os.system(f'cp -rn "{LOCAL_LORA_DIR}"* "{LORA_DIR}/"')
else:
    print(f"⚠️ 注意: LoRA フォルダが見つかりません。スキップします")

# === ✅ WebUI を起動（Hugging Face からの勝手なダウンロードを防ぐ） ===
%cd /content/stable-diffusion-webui
!python launch.py --share --no-download
