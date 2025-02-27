メイン コンテンツにスキップ
Nios_Model_Card_Selection.ipynb のコピー
Nios_Model_Card_Selection.ipynb のコピー_
2023/4/21
有料プランの方のみご利用いただけます。
詳細


[ ]
tree

0.最初にランタイムの設定をGPUに変更してく ださい
「ランタイム」→「ランタイムのタイプを変更」でGPUを選び "保存" をクリック

1.GPUの確認とWebUIのインストール

[ ]
#@title 1.GPUの確認とWebUIのインストール
#GPUの確認
!nvidia-smi

#パッケージインストール
import os
from google.colab import drive

!apt -y update -qq
!apt -y install -qq aria2

ControlNet:

Japanese:

Wed Feb 26 14:03:20 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Tesla T4                       Off |   00000000:00:04.0 Off |                    0 |
| N/A   38C    P8             10W /   70W |       0MiB /  15360MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
28 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)
The following additional packages will be installed:
  libaria2-0 libc-ares2
The following NEW packages will be installed:
  aria2 libaria2-0 libc-ares2
0 upgraded, 3 newly installed, 0 to remove and 28 not upgraded.
Need to get 1,513 kB of archives.
After this operation, 5,441 kB of additional disk space will be used.
Selecting previously unselected package libc-ares2:amd64.
(Reading database ... 124935 files and directories currently installed.)
Preparing to unpack .../libc-ares2_1.18.1-1ubuntu0.22.04.3_amd64.deb ...
Unpacking libc-ares2:amd64 (1.18.1-1ubuntu0.22.04.3) ...
Selecting previously unselected package libaria2-0:amd64.
Preparing to unpack .../libaria2-0_1.36.0-1_amd64.deb ...
Unpacking libaria2-0:amd64 (1.36.0-1) ...
Selecting previously unselected package aria2.
Preparing to unpack .../aria2_1.36.0-1_amd64.deb ...
Unpacking aria2 (1.36.0-1) ...
Setting up libc-ares2:amd64 (1.18.1-1ubuntu0.22.04.3) ...
Setting up libaria2-0:amd64 (1.36.0-1) ...
Setting up aria2 (1.36.0-1) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
/sbin/ldconfig.real: /usr/local/lib/libtcm_debug.so.1 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtcm.so.1 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_0.so.3 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc_proxy.so.2 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbbbind_2_5.so.3 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbbmalloc.so.2 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbbbind.so.3 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libur_loader.so.0 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libur_adapter_opencl.so.0 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libhwloc.so.15 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libumf.so.0 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libtbb.so.12 is not a symbolic link

/sbin/ldconfig.real: /usr/local/lib/libur_adapter_level_zero.so.0 is not a symbolic link

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 GB 550.3 kB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.1/6.1 MB 75.8 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 80.6 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 80.0 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 96.5 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.3/63.3 MB 11.9 MB/s eta 0:00:00
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.4/96.4 kB 3.5 MB/s eta 0:00:00
ERROR: Could not find a version that satisfies the requirement xformers==0.0.19 (from versions: 0.0.1, 0.0.2, 0.0.3, 0.0.4, 0.0.5, 0.0.6, 0.0.7, 0.0.8, 0.0.9, 0.0.10, 0.0.11, 0.0.12, 0.0.13, 0.0.16rc424, 0.0.16rc425, 0.0.16, 0.0.20, 0.0.21, 0.0.22, 0.0.22.post7, 0.0.23, 0.0.23.post1, 0.0.24, 0.0.25, 0.0.25.post1, 0.0.26.post1, 0.0.27, 0.0.27.post1, 0.0.27.post2, 0.0.28, 0.0.28.post1, 0.0.28.post2, 0.0.28.post3, 0.0.29, 0.0.29.post1, 0.0.29.post2, 0.0.29.post3, 0.0.30.dev989, 0.0.30.dev1002)
ERROR: No matching distribution found for xformers==0.0.19
Cloning into 'stable-diffusion-webui'...
remote: Enumerating objects: 33820, done.
remote: Total 33820 (delta 0), reused 0 (delta 0), pack-reused 33820 (from 1)
Receiving objects: 100% (33820/33820), 35.07 MiB | 24.15 MiB/s, done.
Resolving deltas: 100% (23644/23644), done.
Cloning into '/content/stable-diffusion-webui/extensions/sd-webui-ar'...
remote: Enumerating objects: 119, done.
remote: Counting objects: 100% (39/39), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 119 (delta 29), reused 25 (delta 25), pack-reused 80 (from 1)
Receiving objects: 100% (119/119), 26.36 KiB | 3.77 MiB/s, done.
Resolving deltas: 100% (43/43), done.
Cloning into '/content/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser'...
remote: Enumerating objects: 143, done.
remote: Counting objects: 100% (34/34), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 143 (delta 25), reused 22 (delta 22), pack-reused 109 (from 1)
Receiving objects: 100% (143/143), 37.96 KiB | 597.00 KiB/s, done.
Resolving deltas: 100% (51/51), done.
Cloning into '/content/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface'...
remote: Enumerating objects: 124, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 124 (delta 13), reused 11 (delta 10), pack-reused 106 (from 1)
Receiving objects: 100% (124/124), 29.72 KiB | 468.00 KiB/s, done.
Resolving deltas: 100% (43/43), done.
Cloning into '/content/stable-diffusion-webui/extensions/a1111-sd-webui-tagcomplete'...
remote: Enumerating objects: 2438, done.
remote: Counting objects: 100% (726/726), done.
remote: Compressing objects: 100% (298/298), done.
remote: Total 2438 (delta 461), reused 428 (delta 428), pack-reused 1712 (from 2)
Receiving objects: 100% (2438/2438), 14.03 MiB | 14.95 MiB/s, done.
Resolving deltas: 100% (1571/1571), done.
Cloning into '/content/stable-diffusion-webui/extensions/sd-webui-photopea-embed'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 50 (delta 25), reused 41 (delta 21), pack-reused 0 (from 0)
Receiving objects: 100% (50/50), 20.93 KiB | 310.00 KiB/s, done.
Resolving deltas: 100% (25/25), done.
/content/stable-diffusion-webui
Cloning into '/content/stable-diffusion-webui/extensions/openpose-editor'...
remote: Enumerating objects: 361, done.
remote: Counting objects: 100% (95/95), done.
remote: Compressing objects: 100% (35/35), done.
remote: Total 361 (delta 75), reused 69 (delta 60), pack-reused 266 (from 1)
Receiving objects: 100% (361/361), 299.61 KiB | 1.19 MiB/s, done.
Resolving deltas: 100% (154/154), done.
Cloning into '/content/stable-diffusion-webui/extensions/sd-webui-controlnet'...
remote: Enumerating objects: 9979, done.
remote: Counting objects: 100% (819/819), done.
remote: Compressing objects: 100% (100/100), done.
remote: Total 9979 (delta 762), reused 719 (delta 719), pack-reused 9160 (from 2)
Receiving objects: 100% (9979/9979), 18.07 MiB | 17.35 MiB/s, done.
Resolving deltas: 100% (5982/5982), done.
Cloning into '/content/stable-diffusion-webui/extensions/sd-webui-depth-lib'...
remote: Enumerating objects: 98, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 98 (delta 10), reused 9 (delta 9), pack-reused 85 (from 1)
Receiving objects: 100% (98/98), 5.76 MiB | 8.53 MiB/s, done.
Resolving deltas: 100% (19/19), done.
Cloning into '/content/stable-diffusion-webui/extensions/posex'...
remote: Enumerating objects: 407, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 407 (delta 21), reused 40 (delta 21), pack-reused 364 (from 1)
Receiving objects: 100% (407/407), 11.40 MiB | 14.90 MiB/s, done.
Resolving deltas: 100% (196/196), done.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
cf9a44|OK  |   132MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11e_sd15_ip2p_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
82aaf0|OK  |   264MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11e_sd15_shuffle_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
2075f3|OK  |   232MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_canny_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
a18d2d|OK  |    91MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_depth_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
4937a4|OK  |   262MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_inpaint_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
1ca8ab|OK  |   157MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_lineart_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
310927|OK  |   264MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_mlsd_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
30d3e5|OK  |   265MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_normalbae_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f63859|OK  |   257MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_openpose_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
6c5050|OK  |   247MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_scribble_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
6b57bc|OK  |   269MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_seg_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
0be13a|OK  |   264MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_softedge_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
9cf3ca|OK  |   206MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15s2_lineart_anime_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
6fd72d|OK  |   261MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11u_sd15_tile_fp16.safetensors

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
256ceb|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11e_sd15_ip2p_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f573cf|OK  |   322KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11e_sd15_shuffle_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
e783eb|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_canny_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f39b62|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_depth_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
c92fc3|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_inpaint_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
97076e|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_lineart_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
d27e05|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_mlsd_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
3961d8|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_normalbae_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
d8de91|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_openpose_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
4a5641|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_scribble_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
b4b7a0|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_seg_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
121215|OK  |   271KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_softedge_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f65ae4|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15s2_lineart_anime_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
5586e1|OK  |   317KiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11u_sd15_tile_fp16.yaml

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
2a517f|OK  |   242MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_style_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
26e6ca|OK  |   255MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_sketch_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
e48be3|OK  |   203MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_seg_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
634c83|OK  |   244MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_openpose_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
b8d47e|OK  |   241MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_keypose_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
826996|OK  |   258MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_depth_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
f5dead|OK  |   153MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_color_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
d0b1d4|OK  |   244MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_canny_sd14v1.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
8e2a16|OK  |   246MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_canny_sd15v2.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
8eb240|OK  |   212MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_depth_sd15v2.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
414ec9|OK  |   247MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_sketch_sd15v2.pth

Status Legend:
(OK):download completed.

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
fd1527|OK  |   214MiB/s|/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models/t2iadapter_zoedepth_sd15v1.pth

Status Legend:
(OK):download completed.
--2025-02-26 14:07:36--  https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.pt
Resolving huggingface.co (huggingface.co)... 13.249.126.122, 13.249.126.91, 13.249.126.116, ...
Connecting to huggingface.co (huggingface.co)|13.249.126.122|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://cdn-lfs.hf.co/repos/eb/60/eb6088b069ea5caa5dbbaee1920375b51ad5b43576174f06ea781d578f81b8ac/66a7279a88dd0cb17afbc88560540c638336d5783fd6b191c53c0d654e25b9db?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27EasyNegative.pt%3B+filename%3D%22EasyNegative.pt%22%3B&Expires=1740582457&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MDU4MjQ1N319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy9lYi82MC9lYjYwODhiMDY5ZWE1Y2FhNWRiYmFlZTE5MjAzNzViNTFhZDViNDM1NzYxNzRmMDZlYTc4MWQ1NzhmODFiOGFjLzY2YTcyNzlhODhkZDBjYjE3YWZiYzg4NTYwNTQwYzYzODMzNmQ1NzgzZmQ2YjE5MWM1M2MwZDY1NGUyNWI5ZGI%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qIn1dfQ__&Signature=DIShpXDCZ-bSYcqT5NNX3J0SNsWaAkQMDOp882MGmfVlFCbPlvJpXamHRZIfNYkwRYojVHHU8ebektYsFHnjuBMo1I4nRzV6VPXnKXX2v1DxtWdyQpidiNRlcXkxQZbqsZRcFvzcMVuXIyD7jEv3PfSSC8cfCqBx9bYAr-GXzc69saWqiSoyvxlL0gClH8FX5DaVBibi%7ET3EXaF4AUZ2JjXrPi3qAn8A60kT4wRkeRDae7ShnaxGUwgiGH4WabQXKhqz9L5seAcQvMh85FL5P9ubaxywumpydgnY64YpkAip0RcPrroVBjDNKb3xlc2KfEGhbesY%7EhuJR8mhAi4WuQ__&Key-Pair-Id=K3RPWS32NSSJCE [following]
--2025-02-26 14:07:37--  https://cdn-lfs.hf.co/repos/eb/60/eb6088b069ea5caa5dbbaee1920375b51ad5b43576174f06ea781d578f81b8ac/66a7279a88dd0cb17afbc88560540c638336d5783fd6b191c53c0d654e25b9db?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27EasyNegative.pt%3B+filename%3D%22EasyNegative.pt%22%3B&Expires=1740582457&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MDU4MjQ1N319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy9lYi82MC9lYjYwODhiMDY5ZWE1Y2FhNWRiYmFlZTE5MjAzNzViNTFhZDViNDM1NzYxNzRmMDZlYTc4MWQ1NzhmODFiOGFjLzY2YTcyNzlhODhkZDBjYjE3YWZiYzg4NTYwNTQwYzYzODMzNmQ1NzgzZmQ2YjE5MWM1M2MwZDY1NGUyNWI5ZGI%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qIn1dfQ__&Signature=DIShpXDCZ-bSYcqT5NNX3J0SNsWaAkQMDOp882MGmfVlFCbPlvJpXamHRZIfNYkwRYojVHHU8ebektYsFHnjuBMo1I4nRzV6VPXnKXX2v1DxtWdyQpidiNRlcXkxQZbqsZRcFvzcMVuXIyD7jEv3PfSSC8cfCqBx9bYAr-GXzc69saWqiSoyvxlL0gClH8FX5DaVBibi%7ET3EXaF4AUZ2JjXrPi3qAn8A60kT4wRkeRDae7ShnaxGUwgiGH4WabQXKhqz9L5seAcQvMh85FL5P9ubaxywumpydgnY64YpkAip0RcPrroVBjDNKb3xlc2KfEGhbesY%7EhuJR8mhAi4WuQ__&Key-Pair-Id=K3RPWS32NSSJCE
Resolving cdn-lfs.hf.co (cdn-lfs.hf.co)... 3.169.231.87, 3.169.231.4, 3.169.231.38, ...
Connecting to cdn-lfs.hf.co (cdn-lfs.hf.co)|3.169.231.87|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 25323 (25K) [binary/octet-stream]
Saving to: ‘/content/stable-diffusion-webui/embeddings/EasyNegative.pt’

/content/stable-dif 100%[===================>]  24.73K  --.-KB/s    in 0.007s  

2025-02-26 14:07:37 (3.34 MB/s) - ‘/content/stable-diffusion-webui/embeddings/EasyNegative.pt’ saved [25323/25323]

Cloning into '/content/stable-diffusion-webui/extensions/stable-diffusion-webui-localization-ja_JP'...
remote: Enumerating objects: 5539, done.
remote: Counting objects: 100% (794/794), done.
remote: Compressing objects: 100% (322/322), done.
remote: Total 5539 (delta 516), reused 650 (delta 463), pack-reused 4745 (from 1)
Receiving objects: 100% (5539/5539), 2.45 MiB | 5.57 MiB/s, done.
Resolving deltas: 100% (3316/3316), done.
/content/stable-diffusion-webui
2.モデル選択とWebUIの起動

[ ]
#@title  2.モデル選択とWebUIの起動
#@markdown モデル選択とVAEを選択してから実行してください。

import os

model_name ="stable_diffusion_v2.1" #@param ["stable_diffusion_v1.5","stable_diffusion_v2.1","waifu_diffusion_v1.3","Openjourney","anything-v3.0","anything-v4.0","Counterfeit-V2.0","8528-diffusion","AbyssOrangeMix2","EerieOrangeMix2","trinart2_step115000","Eimis_Anime_Diffusion_1.0v","dreamlike-photoreal-2.0","Cyberpunk-Anime-Diffusion","Plat_Diffusion_v1.3.1","ACertainThing","pastel_mix","anything-v4.5","Basil_mix_fixed","Realistic_Vision_V1.3","Counterfeit-V2.5","SukiyakiMix-v1.0","7th_anime_v1.1","7th_anime_v2_C","7th_anime_v3_A","YuzuGinger_v4","YuzuLemonMilk_v1.5", "Defmix-v1.1","RDtMix","Corneo_7th_Heaven_Mix","ChilloutMix","wd-1-5-beta2","AniReality-Mix"] {allow-input: false}

model_dict={
    "stable_diffusion_v1.5":"https://huggingface.co/camenduru/sd15/resolve/main/v1-5-pruned-emaonly.ckpt",
    "stable_diffusion_v2.1":"https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt",
    "waifu_diffusion_v1.3":"https://huggingface.co/hakurei/waifu-diffusion-v1-3/resolve/main/wd-v1-3-float32.ckpt",
    "Openjourney":"https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.safetensors",
    "anything-v3.0":"https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/anything-v3-fp32-pruned.safetensors",
    "anything-v4.0":"https://huggingface.co/ckpt/anything-v4.0/resolve/main/anything-v4.0-pruned.ckpt",
    "anything-v4.5":"https://huggingface.co/ckpt/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors",
    "Counterfeit-V2.0":"https://huggingface.co/gsdf/Counterfeit-V2.0/resolve/main/Counterfeit-V2.0fp16.safetensors",
    "Counterfeit-V2.5":"https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/main/Counterfeit-V2.5_pruned.safetensors",
    "8528-diffusion":"https://huggingface.co/852wa/8528-diffusion/resolve/main/8528d-final.ckpt",
    "AbyssOrangeMix2":"https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_nsfw.safetensors",
    "EerieOrangeMix2":"https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/EerieOrangeMix/EerieOrangeMix2.safetensors",
    "trinart2_step115000":"https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step115000.ckpt",
    "Eimis_Anime_Diffusion_1.0v":"https://huggingface.co/eimiss/EimisAnimeDiffusion_1.0v/resolve/main/EimisAnimeDiffusion_1-0v.ckpt",
    "dreamlike-photoreal-2.0":"https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike-photoreal-2.0.safetensors",
    "Cyberpunk-Anime-Diffusion":"https://huggingface.co/DGSpitzer/Cyberpunk-Anime-Diffusion/resolve/main/Cyberpunk-Anime-Diffusion.ckpt",
    "Plat_Diffusion_v1.3.1":"https://huggingface.co/p1atdev/pd-archive/resolve/main/plat-v1-3-1.safetensors",
    "ACertainThing":"https://huggingface.co/JosephusCheung/ACertainThing/resolve/main/ACertainThing.ckpt",
    "pastel_mix":"https://huggingface.co/andite/pastel-mix/resolve/main/pastelmix-better-vae-fp16.safetensors",
    "Basil_mix_fixed":"https://huggingface.co/nuigurumi/basil_mix/resolve/main/Basil_mix_fixed.safetensors",
    "Realistic_Vision_V1.3":"https://civitai.com/api/download/models/6987",
    "SukiyakiMix-v1.0":"https://huggingface.co/Vsukiyaki/SukiyakiMix-v1.0/resolve/main/SukiyakiMix-v1.0-fp16.safetensors",
    "7th_anime_v1.1":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v1/7th_anime_v1.1.safetensors",
    "7th_anime_v2_A":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v2/7th_anime_v2_A.safetensors",
    "7th_anime_v2_B":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v2/7th_anime_v2_B.safetensors",
    "7th_anime_v2_C":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v2/7th_anime_v2_C.safetensors",
    "7th_anime_v2_G":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v2/7th_anime_v2_G.safetensors",
    "7th_anime_v3_A":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v3/7th_anime_v3_A.safetensors",
    "7th_anime_v3_B":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v3/7th_anime_v3_B.safetensors",
    "7th_anime_v3_C":"https://huggingface.co/syaimu/7th_Layer/resolve/main/7th_anime_v3/7th_anime_v3_C.safetensors",
    "7th_anime_3.1_B":"https://huggingface.co/syaimu/7th_test/resolve/main/7th_anime_3.1_B.ckpt",
    "YuzuGinger_v4":"https://huggingface.co/thiros/YuzuLemonTea/resolve/main/YuzuGinger_v4-pruned.safetensors",
    "YuzuLemonMilk_v1.5":"https://huggingface.co/thiros/YuzuLemonTea/resolve/main/YuzuLemonMilk_v1.5-pruned.safetensors",
    "Defmix-v1.1":"https://huggingface.co/Defpoint/Defmix-v1.0/resolve/main/Defmix-v1.1.safetensors",
    "RDtMix":"https://huggingface.co/Hemlok/DateMix/resolve/main/RDtMix-fp16.safetensors",
    "meadmix":"https://huggingface.co/sazanka-imoto/MeadMix/resolve/main/meadmix.safetensors",
    "Nabylon-v1.0":"https://huggingface.co/NegiInNattoMaki/Nabylon-v1.0/resolve/main/Nabylon-v1.0-fp16.safetensors",
    "LonganMix":"https://huggingface.co/Hemlok/LonganMix/resolve/main/LonganMix-fp16.ckpt",
    "Corneo_7th_Heaven_Mix":"https://civitai.com/api/download/models/5338",
    "Corneo_Shinra26_Mix":"https://civitai.com/api/download/models/6918",
    "atwmix_test2":"https://huggingface.co/atsuwo/atwmix_test2/resolve/main/atwmix_test2.ckpt",
    "Graham_Special":"https://huggingface.co/Graham-san/Graham_Special/resolve/main/Graham%20Special%20v1.ckpt",
    "BalorV2featAbyssOrange2":"https://huggingface.co/ploughB660/Balor-V2/resolve/main/BalorV2featAbyssOrange2.safetensors",
    "Balor-V2.5featAOM3A3":"https://huggingface.co/ploughB660/Balor-V3/resolve/main/Balor-V2.5featAOM3A3.safetensors",
    "ChilloutMix":"https://civitai.com/api/download/models/11745",
    "wd-1-5-beta2":"https://huggingface.co/waifu-diffusion/wd-1-5-beta2/resolve/main/checkpoints/wd-1-5-beta2-aesthetic-fp16.safetensors",
    "AniReality-Mix":"https://civitai.com/api/download/models/33305"
}


vae_name = "Anything-V3.0" #@param ["","vae-ft-mse-840000-ema-pruned","vae-ft-mse-560000-ema-pruned","kl-f8-anime","kl-f8-anime2","Anything-V3.0","anything-v4.0","autoencoder_fix_kl-f8-trinart_characters","orangemix"] {allow-input: false}

url_dict = {
    "vae-ft-mse-840000-ema-pruned": "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors",
    "vae-ft-mse-560000-ema-pruned": "https://huggingface.co/stabilityai/sd-vae-ft-ema-original/resolve/main/vae-ft-ema-560000-ema-pruned.ckpt",
    "kl-f8-anime": "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime.ckpt",
    "kl-f8-anime2": "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt",
    "Anything-V3.0": "https://huggingface.co/ckpt/anything-v3.0/resolve/main/Anything-V3.0.vae.pt",
    "anything-v4.0":"https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.0.vae.pt",
    "autoencoder_fix_kl-f8-trinart_characters": "https://huggingface.co/naclbit/trinart_characters_19.2m_stable_diffusion_v1/resolve/main/autoencoder_fix_kl-f8-trinart_characters.ckpt",
    "orangemix": "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt",
}

model_url = model_dict.get(model_name)
vae_url = url_dict.get(vae_name)

def install(model_url, vae_url):

    if model_url :
        base_name = os.path.basename(model_url)
        if model_url.startswith("https://drive.google.com"):
            os.chdir("/content/stable-diffusion-webui/models/Stable-diffusion")
            !gdown --fuzzy {model_url}
        elif model_url.startswith("https://huggingface.co/"):
            if "/blob/" in model_url:
                model_url = model_url.replace("/blob/", "/resolve/")
            huggingface_token ="YOUR_HUGGINGFACE_TOKEN" # 自分のトークンに変更
            user_header = f'"Authorization: Bearer {huggingface_token}"'
            !wget --no-check-certificate --header={user_header} {model_url} -O /content/stable-diffusion-webui/models/Stable-diffusion/{base_name}
        else:
            !wget {model_url} -O /content/stable-diffusion-webui/models/Stable-diffusion/{model_name}.safetensors
    if vae_url :
        base_name = os.path.basename(vae_url)
        !wget {vae_url} -O /content/stable-diffusion-webui/models/VAE/{base_name}

install(model_url, vae_url)

%cd /content/stable-diffusion-webui
!sed -i -e '''/prepare_environment()/a\    os.system\(f\"""sed -i -e ''\"s/dict()))/dict())).cuda()/g\"'' /content/stable-diffusion-webui/repositories/stable-diffusion-stability-ai/ldm/util.py""")''' /content/stable-diffusion-webui/launch.py
!python launch.py --share --xformers --enable-insecure-extension-access --gradio-queue --no-half-vae
モデル選択とVAEを選択してから実行してください。

model_name:
stable_diffusion_v2.1
vae_name:
Anything-V3.0
--2025-02-26 14:13:54--  https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt
Resolving huggingface.co (huggingface.co)... 18.164.174.17, 18.164.174.55, 18.164.174.118, ...
Connecting to huggingface.co (huggingface.co)|18.164.174.17|:443... connected.
HTTP request sent, awaiting response... 401 Unauthorized

Username/Password Authentication Failed.
--2025-02-26 14:13:54--  https://huggingface.co/ckpt/anything-v3.0/resolve/main/Anything-V3.0.vae.pt
Resolving huggingface.co (huggingface.co)... 18.164.174.17, 18.164.174.118, 18.164.174.23, ...
Connecting to huggingface.co (huggingface.co)|18.164.174.17|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://cdn-lfs.hf.co/repos/43/3b/433bc34278d232abc26eacd1755075b8526959b10c4fa7332f4269bf9e9b4b6e/f921fb3f29891d2a77a6571e56b8b5052420d2884129517a333c60b1b4816cdf?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27Anything-V3.0.vae.pt%3B+filename%3D%22Anything-V3.0.vae.pt%22%3B&Expires=1740582835&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MDU4MjgzNX19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy80My8zYi80MzNiYzM0Mjc4ZDIzMmFiYzI2ZWFjZDE3NTUwNzViODUyNjk1OWIxMGM0ZmE3MzMyZjQyNjliZjllOWI0YjZlL2Y5MjFmYjNmMjk4OTFkMmE3N2E2NTcxZTU2YjhiNTA1MjQyMGQyODg0MTI5NTE3YTMzM2M2MGIxYjQ4MTZjZGY%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qIn1dfQ__&Signature=YXaS-MhBqQlm8TCy-OxzPktedIsKpKrK6AUJohIk%7EEoKHOcesBHkabUcHwzefFdPFOj0nliYjZXqBF-086T-MUSrleHOlbdGhrbEinpoFxU%7EtkBCi2pIbdJQW%7EdL1ZLNJ9MX5F1KSzng6ZHGZdPBJCxjLRq1CQZAtHCAXoo5kzrMKaO1AeNO35H4Xj8WMkoMEQGu38EH1h2Iz5pKeTCK5HagQ3drdWDfJs-I7S8ZAWEcXKWwHfu8oEn4G7WvHWMeEx-3U4Fbfuh-lJ0U8tgo%7EjDsN%7EdTT0SWvpOYE%7EQSM9iHhkSdYQYPX87Lu9gk1oVQg7CxNg75nEoVCsT6iq13sg__&Key-Pair-Id=K3RPWS32NSSJCE [following]
--2025-02-26 14:13:55--  https://cdn-lfs.hf.co/repos/43/3b/433bc34278d232abc26eacd1755075b8526959b10c4fa7332f4269bf9e9b4b6e/f921fb3f29891d2a77a6571e56b8b5052420d2884129517a333c60b1b4816cdf?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27Anything-V3.0.vae.pt%3B+filename%3D%22Anything-V3.0.vae.pt%22%3B&Expires=1740582835&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MDU4MjgzNX19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy80My8zYi80MzNiYzM0Mjc4ZDIzMmFiYzI2ZWFjZDE3NTUwNzViODUyNjk1OWIxMGM0ZmE3MzMyZjQyNjliZjllOWI0YjZlL2Y5MjFmYjNmMjk4OTFkMmE3N2E2NTcxZTU2YjhiNTA1MjQyMGQyODg0MTI5NTE3YTMzM2M2MGIxYjQ4MTZjZGY%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qIn1dfQ__&Signature=YXaS-MhBqQlm8TCy-OxzPktedIsKpKrK6AUJohIk%7EEoKHOcesBHkabUcHwzefFdPFOj0nliYjZXqBF-086T-MUSrleHOlbdGhrbEinpoFxU%7EtkBCi2pIbdJQW%7EdL1ZLNJ9MX5F1KSzng6ZHGZdPBJCxjLRq1CQZAtHCAXoo5kzrMKaO1AeNO35H4Xj8WMkoMEQGu38EH1h2Iz5pKeTCK5HagQ3drdWDfJs-I7S8ZAWEcXKWwHfu8oEn4G7WvHWMeEx-3U4Fbfuh-lJ0U8tgo%7EjDsN%7EdTT0SWvpOYE%7EQSM9iHhkSdYQYPX87Lu9gk1oVQg7CxNg75nEoVCsT6iq13sg__&Key-Pair-Id=K3RPWS32NSSJCE
Resolving cdn-lfs.hf.co (cdn-lfs.hf.co)... 3.169.231.87, 3.169.231.115, 3.169.231.38, ...
Connecting to cdn-lfs.hf.co (cdn-lfs.hf.co)|3.169.231.87|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 822802803 (785M) [binary/octet-stream]
Saving to: ‘/content/stable-diffusion-webui/models/VAE/Anything-V3.0.vae.pt’

/content/stable-dif 100%[===================>] 784.69M  42.4MB/s    in 16s     

2025-02-26 14:14:11 (50.2 MB/s) - ‘/content/stable-diffusion-webui/models/VAE/Anything-V3.0.vae.pt’ saved [822802803/822802803]

/content/stable-diffusion-webui
sed: can't read /content/stable-diffusion-webui/repositories/stable-diffusion-stability-ai/ldm/util.py: No such file or directory
Python 3.11.11 (main, Dec  4 2024, 08:55:07) [GCC 11.4.0]
Commit hash: 22bcc7be428c94e9408f589966c2040187245d81
Installing gfpgan
Installing clip
Installing open_clip
Installing xformers
Traceback (most recent call last):
  File "/content/stable-diffusion-webui/launch.py", line 356, in <module>
    prepare_environment()
  File "/content/stable-diffusion-webui/launch.py", line 282, in prepare_environment
    run_pip(f"install {xformers_package}", "xformers")
  File "/content/stable-diffusion-webui/launch.py", line 129, in run_pip
    return run(f'"{python}" -m pip {args} --prefer-binary{index_url_line}', desc=f"Installing {desc}", errdesc=f"Couldn't install {desc}")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/content/stable-diffusion-webui/launch.py", line 97, in run
    raise RuntimeError(message)
RuntimeError: Couldn't install xformers.
Command: "/usr/bin/python3" -m pip install xformers==0.0.16rc425 --prefer-binary
Error code: 1
stdout: Collecting xformers==0.0.16rc425
  Downloading xformers-0.0.16rc425.tar.gz (7.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 32.5 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: torch>=1.12 in /usr/local/lib/python3.11/dist-packages (from xformers==0.0.16rc425) (2.0.0+cu118)
Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (from xformers==0.0.16rc425) (1.26.4)
Collecting pyre-extensions==0.0.23 (from xformers==0.0.16rc425)
  Downloading pyre_extensions-0.0.23-py3-none-any.whl.metadata (4.0 kB)
Collecting typing-inspect (from pyre-extensions==0.0.23->xformers==0.0.16rc425)
  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.11/dist-packages (from pyre-extensions==0.0.23->xformers==0.0.16rc425) (4.12.2)
Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from torch>=1.12->xformers==0.0.16rc425) (3.17.0)
Requirement already satisfied: sympy in /usr/local/lib/python3.11/dist-packages (from torch>=1.12->xformers==0.0.16rc425) (1.13.1)
Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (from torch>=1.12->xformers==0.0.16rc425) (3.4.2)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from torch>=1.12->xformers==0.0.16rc425) (3.1.5)
Requirement already satisfied: triton==2.0.0 in /usr/local/lib/python3.11/dist-packages (from torch>=1.12->xformers==0.0.16rc425) (2.0.0)
Requirement already satisfied: cmake in /usr/local/lib/python3.11/dist-packages (from triton==2.0.0->torch>=1.12->xformers==0.0.16rc425) (3.31.4)
Requirement already satisfied: lit in /usr/local/lib/python3.11/dist-packages (from triton==2.0.0->torch>=1.12->xformers==0.0.16rc425) (18.1.8)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->torch>=1.12->xformers==0.0.16rc425) (3.0.2)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy->torch>=1.12->xformers==0.0.16rc425) (1.3.0)
Collecting mypy-extensions>=0.3.0 (from typing-inspect->pyre-extensions==0.0.23->xformers==0.0.16rc425)
  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Downloading pyre_extensions-0.0.23-py3-none-any.whl (11 kB)
Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Building wheels for collected packages: xformers
  Building wheel for xformers (setup.py): started
  Building wheel for xformers (setup.py): finished with status 'error'
  Running setup.py clean for xformers
Failed to build xformers

stderr:   error: subprocess-exited-with-error
  
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for xformers
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (xformers)


生成した画像の利用については自己判断および自己責任でお願いします。

▼より高速な画像生成を行いたい方向け
ColabのProに加入するよりもPaperspaceを使用することをおすすめします。

モデルを切り替えたい場合
・2の実行を止めモデルを選択し直す。 その後、再度2を実行する。
・もしくは、モデルを選択し直し、ヘッダーの「ランタイム」→「再起動して全てのセルを実行」を選び "はい" をクリック

▼使い方
Google Colabで画像生成AIの色々なモデルを簡単に使おう

▼学習済みモデルの検索
HuggingFace

▼Colabページの説明
stable-diffusion-webui-colab-japanese

▼上級者向け
Nios_v2_update.ipynb
Nios_v3.ipynb

Colab の有料サービス - 契約解除はこちら
