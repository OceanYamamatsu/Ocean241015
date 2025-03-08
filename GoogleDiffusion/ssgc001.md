# 25/03/02

# ランタイムをGPUに設定することを推奨
import os

# 不要なパッケージを削除（wandbなし）
!pip uninstall -y wandb

# 必要なパッケージのインストール
!apt -y update -qq
!apt -y install -qq aria2 git

# WebUIのインストール
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git /content/stable-diffusion-webui

# Hugging Faceのトークンを環境変数に設定（自分のトークンを入力）
os.environ["HUGGINGFACE_TOKEN"] = "aaaaaaaaaaaaaaaaaaaaaa"

# モデルとVAEのURLを設定
MODEL_URL = "https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt"

VAE_URL = "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors"

# モデルとVAEの保存先
MODEL_DIR = "/content/stable-diffusion-webui/models/Stable-diffusion"
VAE_DIR = "/content/stable-diffusion-webui/models/VAE"

# ディレクトリが存在しない場合は作成
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(VAE_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "model.safetensors")
VAE_PATH = os.path.join(VAE_DIR, "vae.safetensors")

# aria2で高速ダウンロード
def download_model(url, output_path):
    !aria2c --header="Authorization: Bearer $HUGGINGFACE_TOKEN" -o {output_path} {url}

# モデルとVAEをダウンロード
download_model(MODEL_URL, MODEL_PATH)
download_model(VAE_URL, VAE_PATH)

# Web UIの起動
%cd /content/stable-diffusion-webui
!python launch.py --share --no-half-vae --enable-insecure-extension-access --gradio-queue