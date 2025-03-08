ローカルにある **checkpoint（.safetensors, .ckpt）** と **LoRA** を使用するようにコードを変更します。具体的には、以下のように修正します。

### **変更点**
1. **Hugging Faceからのモデルダウンロードを削除**
2. **ローカルにあるモデルとLoRAのパスを指定**
3. **Web UIの起動オプションを適切に設定**

### **修正後のコード**
```python
import os

# ランタイムをGPUに設定することを推奨
# 不要なパッケージを削除（wandbなし）
!pip uninstall -y wandb

# 必要なパッケージのインストール
!apt -y update -qq
!apt -y install -qq aria2 git

# WebUIのインストール
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git /content/stable-diffusion-webui

# ローカルのモデルとLoRAのパスを設定
LOCAL_MODEL_PATH = "/content/drive/MyDrive/StableDiffusion/models/model.safetensors"  # ここにローカルのモデルパスを指定
LOCAL_VAE_PATH = "/content/drive/MyDrive/StableDiffusion/models/vae.safetensors"  # ここにVAEのパスを指定
LOCAL_LORA_DIR = "/content/drive/MyDrive/StableDiffusion/lora/"  # LoRAフォルダのパス

# WebUIのモデルフォルダ
MODEL_DIR = "/content/stable-diffusion-webui/models/Stable-diffusion"
VAE_DIR = "/content/stable-diffusion-webui/models/VAE"
LORA_DIR = "/content/stable-diffusion-webui/models/Lora"

# ディレクトリが存在しない場合は作成
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(VAE_DIR, exist_ok=True)
os.makedirs(LORA_DIR, exist_ok=True)

# モデルとVAEをコピー
!cp {LOCAL_MODEL_PATH} {MODEL_DIR}/model.safetensors
!cp {LOCAL_VAE_PATH} {VAE_DIR}/vae.safetensors

# LoRAフォルダの中身をコピー
!cp -r {LOCAL_LORA_DIR}* {LORA_DIR}/

# Web UIの起動
%cd /content/stable-diffusion-webui
!python launch.py --share --no-half-vae --enable-insecure-extension-access --gradio-queue
```

---

### **説明**
- `LOCAL_MODEL_PATH` にローカルの `.safetensors` や `.ckpt` モデルのパスを指定
- `LOCAL_VAE_PATH` にローカルの VAE ファイルのパスを指定
- `LOCAL_LORA_DIR` にLoRAの保存フォルダを指定し、`/models/Lora/` にコピー
- **`aria2c` でのダウンロード部分を削除**
- **Web UI をローカルのモデルで起動**

---

### **ローカルファイルを使用するメリット**
- モデルのダウンロード不要 → **起動が速い**
- 自分の環境で調整した **LoRAやVAEがすぐ使える**
- **Colabの制限**（ダウンロード速度やHugging Faceのトークン制限）を回避

この方法でローカルのモデルとLoRAを使用できます。試してみてください！ 🚀