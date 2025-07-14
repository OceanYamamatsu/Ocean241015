# [2] Google Drive をマウント
from google.colab import drive
drive.mount('/content/drive')


# [1] PyTorch & xformers の準備（CU121対応）
!pip uninstall -y torch torchvision torchaudio xformers triton
# PyTorch 2.1.2 + xformers 0.0.23.post1 を CU121 向けにインストール
!pip install torch==2.1.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
!pip install xformers==0.0.23.post1


# [3] WebUI 本体をDriveからリンク
import os
drive_webui_path = "/content/drive/MyDrive/sd_pasm/stable-diffusion-webui"
target_webui_path = "/content/stable-diffusion-webui"

if not os.path.exists(target_webui_path):
    os.symlink(drive_webui_path, target_webui_path)


# [4] LoRA 拡張機能もDriveからリンク
ext_src = "/content/drive/MyDrive/sd_pasm/sd-webui-additional-networks"
ext_dst = "/content/stable-diffusion-webui/extensions/sd-webui-additional-networks"

if not os.path.exists(ext_dst):
    os.symlink(ext_src, ext_dst)


# [5] モデル・LoRA のコピー
import shutil
model_src = "/content/drive/MyDrive/checkpoint_nila/JANKUV4NSFWTrainedNoobaiEPS_v40.safetensors"
lora_src = "/content/drive/MyDrive/sd_mika"
model_dst = "/content/stable-diffusion-webui/models/Stable-diffusion"
lora_dst = "/content/stable-diffusion-webui/models/Lora"
os.makedirs(model_dst, exist_ok=True)
os.makedirs(lora_dst, exist_ok=True)
# モデルをコピー（必要に応じて rename）
if os.path.exists(model_src):
    shutil.copy2(model_src, os.path.join(model_dst, "model.safetensors"))
# LoRA をすべてコピー
if os.path.exists(lora_src):
    for file in os.listdir(lora_src):
        src = os.path.join(lora_src, file)
        dst = os.path.join(lora_dst, file)
        if os.path.isfile(src):
            shutil.copy2(src, dst)


# [6] WebUI の起動
%cd /content/stable-diffusion-webui
!python launch.py --share --no-half-vae --enable-insecure-extension-access --gradio-queue --skip-torch-cuda-test --xformers
#!python launch.py --share --medvram --xformers --no-half-vae --enable-insecure-extension-access --gradio-queue --skip-torch-cuda-test
