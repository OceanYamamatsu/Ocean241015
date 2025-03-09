

import os

# === ✅ 不要なパッケージを削除 ===
!pip uninstall -y wandb

# === ❗❗ 必ずここをあなたの環境に合わせて修正してください ❗❗ ===
LOCAL_MODEL_PATH = "/path/to/your/local/model.safetensors"  # 例: "/content/drive/MyDrive/sd_model/model.safetensors"
LOCAL_VAE_PATH = "/path/to/your/local/vae.safetensors"  # 例: "/content/drive/MyDrive/sd_model/vae.safetensors"
LOCAL_LORA_DIR = "/path/to/your/local/lora/"  # 例: "/content/drive/MyDrive/sd_model/lora/"

# === WebUI のフォルダ設定 ===
MODEL_DIR = "/content/stable-diffusion-webui/models/Stable-diffusion"
VAE_DIR = "/content/stable-diffusion-webui/models/VAE"
LORA_DIR = "/content/stable-diffusion-webui/models/Lora"

# フォルダを作成（すでにある場合はスキップ）
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(VAE_DIR, exist_ok=True)
os.makedirs(LORA_DIR, exist_ok=True)

# === ✅ モデルと VAE を WebUI にコピー（既存のものは上書きしない） ===
if os.path.exists(LOCAL_MODEL_PATH):
    os.system(f'cp -n "{LOCAL_MODEL_PATH}" "{MODEL_DIR}/model.safetensors"')
else:
    print(f"🚨 エラー: モデルファイルが見つかりません！ {LOCAL_MODEL_PATH} を確認してください")

if os.path.exists(LOCAL_VAE_PATH):
    os.system(f'cp -n "{LOCAL_VAE_PATH}" "{VAE_DIR}/vae.safetensors"')
else:
    print(f"⚠️ 注意: VAE が見つかりません。スキップします")

# === ✅ LoRA フォルダの中身を WebUI にコピー（フォルダごとコピー） ===
if os.path.exists(LOCAL_LORA_DIR):
    os.system(f'cp -rn "{LOCAL_LORA_DIR}"* "{LORA_DIR}/"')
else:
    print(f"⚠️ 注意: LoRA フォルダが見つかりません。スキップします")

# === ✅ WebUI を起動（Hugging Face からの勝手なダウンロードを防ぐ） ===
%cd /content/stable-diffusion-webui
!python launch.py --share --no-download



