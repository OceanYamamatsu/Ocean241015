チャット履歴



ChatGPT
チャットGPT

GPTを探索する
今日
2024年
アップグレードプラン
最高のモデルにもっとアクセス

チャットGPT

共有する

ユーザー
あなた:
ログイン NovelAIよりもすごい？ AnythingV3をGoogle Colabで挑戦！ 2022/11/13に公開 2023/01/16 16件 AI Stable Diffusion anything tech 最新のAnythingV4が出たので記事を書きました！この記事は基本的に StableDiffusion をモデルを差し替えて試してみるのとほぼ同等で、Google Colab ではじめる Trinart Stable Diffusion の記事を参考にさせていただきました。大変ありがとうございます。無料の実行ランタイムで動くので、ちょっと重いけどお金もかかりません。 注意 (反省) AnythingV3 のモデルについては出自については怪しい、NovelAI また、一部のモデルファイルに関して、ウイルススキャンした結果、新規トロイの木馬が検出されたという話もあります。 Colab のノートブックを作成し、「編集 → ノートブックの設定」からハードウェアアクセラレータを「GPU」に選択します。 その後、以下のコードセルを追加して実行し、GPU が動く最高を確認します。 # GPU の確認 !nvidia-smi 実行環境の次に、コードセルを追加し、以下のパッケージをインストールします。 git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers !pip install pytorch_lightning tensorboard==2.9.1 omegaconf einops taming-transformers==0.0.1クリップトランスフォーマーコルニアテストチューブ!pipインストールディフューザー不可視ウォーターマークこの過程において、ランタイムの再起動が要求されるので、[ランタイム → ランタイムを再起動]で再起動をしておくことをお勧めします。その後、StableDiffusionをインストールします。画像生成の実行は、stable-diffusionのフォルダ内で実行します。 #StableDiffusionのインストール !gitクローン https://github.com/CompVis/stable-diffusion.git %cdsteady-diffusion !pip install -e 。 %mkdir 出力 次に、AnythingV3.0 のモデルデータをダウンロードします。モデルデータは Linaqruf/anything-v3.0 に複数のパターンが存在しますが、Google Colab の RAM の都合上、フルのモデルデータ (7.7GB) ではなく、注目されたモデルデータ (3.8GB) のものを利用します。 # Anythingv3.0 のモデルデータを取得します !wget https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt これで実行に必要なデータは一通り揃いました。 実行テキストから画像生成のため、コードセルを追加し、例として、以下のように実行します。 --prompt "かわいい猫耳メイド"で指定している部分がプロンプトと呼ばれる、どのような画像を生成してほしいと指定する呪文の箇所になります。 ./Anything-V3.0-pruned.ckpt \ --skip_grid \ --n_samples 1 \ --n_iter 1 \ --outdir Outputs \ --ddim_steps 100 \ --prompt "かわいい猫耳メイド" その後、左メニューのファイルから、/content/stable-diffusion/outputs 以下に作成されたファイルが確認できます。ダウンロードもできるので、好きなように使ってください。に上げるときはぜひプロンプトと共に共有してくれると、呪文の解析がみんなハッピーになれます。 作業効率を上げるためにも、作成した画像をGoogle Driveにマウントしたフォルダに上げるなど、工夫をしてみるのもいいかもしれません。と感じる内容のものはほとんどなく、あまりこのフィルターが意味を成しているようには見えません。そのため、作業の邪魔であるセーフフィルターを 以下に自分が作成したセーフフィルタを削除したtxt2img.pyをダウンロードして、場所に展開します。 https://gist.githubusercontent.com/uakihir0/bbb1bd8a4480e2bab07726ca0e744f91/raw/3e6f43fa5c112e512006cc9e33e932f6c6539d94/txt2img。py -O scripts/txt2img2.py このファイルを置くには以下のように、python の実行ファイル名を変更して実行します。オプションの内容は特に変更することで内部使用することができます。 # テキストからの画像生成 !python scripts/txt2img2.py \ # ... (略) ... Stable Diffusion Web UI 対応 また、Web UI上で生成する画像に対してのプロンプトやステップ数などの設定ができる Stable Diffusion web UI に対応し、便利になった方がいましたので、ここで紹介させて頂ければと思います。ありがとうございます。 意外と簡単に遊べるので、AIイラストってどうなの？プログラマー | Swift/Kotlin/Go |世界ソーシャルハブ ​​|かくだけ.net | www.uakihir0.com/ブログ | twitter.com/uakihir0 | misskey.io/@uakihir0 フォロー ディスカッション Plat Plat 2022/11/15 Anything-V3.0はNovelAIのリークモデルをもとに作られている可能性が大きいうえ、はっきりと出自が不明だったり、一部のckptがウイルスチェックにひっかかっているため、その点を説明せずにただの強いイラストモデルとして紹介するのはよくないと思います... 1 うるしうるし2022/11/15に更新確実に、ちょっと用意できないと思いますので、記事の最初の方にモデルについての注意書きを書きました。ありがとうございます。 コメントを追加 taka taka 2022/11/16 記事参考にさせていただいて、自分のgoogle colabの環境でやってみたのですが、下記のようなエラーが出てしまいました。 (最新の呼び出しは最後): ldm.models.diffusion.dpm_solver import の <module> 内のファイル「scripts/txt2img.py」、行 20 DPMSolverSampler ファイル「/content/stable-diffusion/ldm/models/diffusion/dpm_solver/init.py」、1 行目、.sampler import からの <module> 内 DPMSolverSampler ファイル「/content/stable-diffusion/ldm/models/diffusion/dpm_solver/sampler.py」、5 行目、.solver import からの <module> NoiseScheduleVP、model_wrapper、DPM_Solver ModuleNotFoundError: 'ldm.models.diffusion.dpm_solver.solver' という名前のモジュールがありません ''' 2 うるし うるし 2022/11/17 !pip install diffusers がうまく実行されていないように見えます。上記でライブラリがインストールされます。を再接続した場合、実行したすべての内容がリセットされるので、もう一度一番上から順次実行してみてください。 taka taka 2022/11/17 ありがとうございます。 問題なく実行できました。 https://github.com/CompVis/stable-diffusion/blob/main/scripts/txt2img.py 見るといろんなオプションが確認できると思います。縦横サイズについては、画像を生成するコマンドに以下を追加してみてください。(512はサイズです) --H 512 --W 512で変更が可能です。大きすぎると、Google ColabのRAMサイズでは生成が難しいかもしれません。 yuyu 2022/11/17 ありがとうございます。 コマンドを追加してみたの下記のようなエラーが出て画像が生成できませんでした。 このエラーはRAMサイズが原因でエラーになるのでお願いします。 2022/11/17 縦横のサイズは 64 の倍数であるという条件があるので、そこにあったのではないかと思います。 yuyu yuyu 2022/11/17 なんとかありがとうございます。返信を追加 so-shi so-shi 2022/11/26 記事を参考にさせていただいております。 １点お楽しみしたいのですが、Google Colab 上でフルバージョンのモデルを使用することは不可能なのでお願いしますか? 1 うるし うるし 2022/11/28 無料の範囲内の場合は、RAM不足せずにフルバージョンは読み込めませんでした。 そのうち、プランを変更して、大きなRAMが使用できる場合は読み込めるのではないかと思います。セーフフィルタが働いているので、その画像が出力されます。セーフフィルタの削除を試してみてください。 2023/01/14 はじめまして、こちらの記事のおかげで導入できましたありがとうございます Anything V3 – Better VAE にバージョンがアップしていて全体にパフォーマンスがありますが、導入がうまくできません ここの説明がとてもわかりやすいので紹介していただけると嬉しいです ログインするとコメントできます ログイン うるし うるし フォロー Urushihara Akihiro | 2023/01/14プログラマー | Swift/Kotlin/Go |世界ソーシャルハブ ​​|かくだけ.net | www.uakihir0.com/ブログ | twitter.com/uakihir0 | misskey.io/@uakihir0 最新のAnythingV4が出たので記事を書きました！ (追記) はじめに注意 (追記) 手順まとめ Zennからのお知らせ 記事投稿コンテスト開催中！ 期間: 2024/12/25まで エンジニアのための情報共有コミュニティ About Zennについて 運営会社お知らせ・リリース Guides 使い方 法人向けメニュー New Publication / Pro よくある質問 Links X(Twitter) GitHub メディアキット Legal利用規約 プライバシーポリシー 特商法表記 Classmethod inc.
チャットGPT:
この記事は、「Anything V3」という安定拡散ベースのAIイラスト生成モデルをGoogle Colabを利用して挑戦する方法について説明しています。以下、重要なポイントをまとめます。

1.モデル概要
Anything V3は、Stable Diffusionの派生モデルで、簡単なプロンプト（呪文）で高品質な画像生成が可能です。
ハグフェイスにアップされているモデルを利用。
無料のGoogle Colabでも動作可能です。尚、以下の注意が必要です。
に関する問題から出ています: NovelAI のリークモデルを基にしている可能性。
安全の危機: 一部でウイルスが検出されたという報告があり、利用は自己責任です。
2. Google Colabを使ったセットアップ手順
（１）環境構築
Google Colabで新規ノートブックを作成し、ハードウェアアクセラレータをGPUに設定します。
必要なライブラリと安定拡散をインストール：
!pip install -e git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers
!pip install pytorch_lightning tensorboard==2.9.1 omegaconf einops taming-transformers==0.0.1 clip transformers kornia test-tube
!pip install diffusers invisible-watermark
!git clone https://github.com/CompVis/stable-diffusion.git
%cd stable-diffusion
!pip install -e .
%mkdir outputs
(2)モデルのダウンロード
Linaqrufが提供するAnything V3.0モデル（軽量版）をダウンロード：
!wget https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt
(3) 画像生成
プロンプトを指定して画像を生成する：
!python scripts/txt2img.py \
    --plms \
    --ckpt ./Anything-V3.0-pruned.ckpt \
    --skip_grid \
    --n_samples 1  \
    --n_iter 1 \
    --outdir outputs \
    --ddim_steps 100 \
    --prompt "cute cat ear maid"
3.補足情報
(1) セーフフィルタの除去
NSFWフィルタを有効化するため、txt2img.pyカスタマイズ：
!wget https://gist.githubusercontent.com/uakihir0/bbb1bd8a4480e2bab07726ca0e744f91/raw/3e6f43fa5c112e512006cc9e33e932f6c6539d94/txt2img.py -O scripts/txt2img2.py
カスタマイズ版のスクリプトを使って実行：
!python scripts/txt2img2.py \
    --plms \
    --ckpt ./Anything-V3.0-pruned.ckpt \
    --prompt "cute cat ear maid"
(2) 解像度設定
画像サイズを指定するオプション：
--H 512 --W 512
※64の倍数で指定する必要があります。
4.制限と課題
RAM容量の制限: Google Colab無料版ではフルバージョンのモデルを読み込めません。
エラー対応: 必要なモジュールがインストールされていない場合、最初から順次コードを実行し直します。
プロンプトの設定:出力品質はプロンプトによって変動します。SNSで共有するとプロンプト解析が進みます。
5.最新バージョンへの対応
記事執筆時点では、Anything V4や「Better VAE」など、性能向上したバージョンも存在します。
この手順を利用して、Google Colab で簡単に AI イラスト生成を行うことが可能です。







あなた:
まとめる
チャットGPT:
以下は、Google Colabで「Anything V3」をセットアップし、画像生成を実行するためのコードをまとめたものです。これを順に実行すればセットアップが完了し、画像生成がうまくいきます。

1. GPUの確認
# GPUの確認
!nvidia-smi
2.必要なライブラリのインストール
# 必要なライブラリをインストール
!pip install -e git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers
!pip install pytorch_lightning tensorboard==2.9.1 omegaconf einops taming-transformers==0.0.1 clip transformers kornia test-tube
!pip install diffusers invisible-watermark
3. 安定拡散のセットアップ
# Stable Diffusionのクローンとセットアップ
!git clone https://github.com/CompVis/stable-diffusion.git
%cd stable-diffusion
!pip install -e .
%mkdir outputs
4.モデルのダウンロード
# Anything V3.0モデル（軽量版）のダウンロード
!wget https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt
5. 画像生成
以下のコードを実行して画像を生成します。--prompt生成したい画像の説明を入力してください。

# テキストから画像を生成
!python scripts/txt2img.py \
    --plms \
    --ckpt ./Anything-V3.0-pruned.ckpt \
    --skip_grid \
    --n_samples 1 \
    --n_iter 1 \
    --outdir outputs \
    --ddim_steps 100 \
    --prompt "cute cat ear maid"
6. オプション（画像サイズ変更）
画像の解像度を指定する場合は、以下のオプションを追加してください（サイズは64の倍数）。

--H 512 --W 512
例：

!python scripts/txt2img.py \
    --plms \
    --ckpt ./Anything-V3.0-pruned.ckpt \
    --skip_grid \
    --n_samples 1 \
    --n_iter 1 \
    --outdir outputs \
    --ddim_steps 100 \
    --H 512 --W 512 \
    --prompt "beautiful landscape with mountains"
注意
RAM容量の制限: 無料版ColabではRAM不足でフルモデルは使用できません。
セーフフィルタの削除: 必要に応じて、フィルタを無効化したカスタマイズ版スクリプト（txt2img2.py）を使用できます。
実行後
生成された画像は以下のフォルダに保存されます：

/content/stable-diffusion/outputs
このコードをColabにコピーペーストすることで、簡単に挑戦できます！







あなた:
セーフフィルタの削除はどこに書き込む
チャットGPT:
セーフフィルタを削除するには、Google Colab 環境にカスタマイズされたスクリプト（txt2img2.py）をダウンロードし、それを使って画像生成を実行する必要があります。

1. セーフセキュリティ削除スクリプトのダウンロード
以下のコードを追加して、セーフ新しいフィルタを削除したカスタム スクリプトを取得します。このスクリプトは既知の上書きtxt2img.pyせず、名前で保存します。

# セーフフィルタを除去したスクリプトのダウンロード
!wget https://gist.githubusercontent.com/uakihir0/bbb1bd8a4480e2bab07726ca0e744f91/raw/3e6f43fa5c112e512006cc9e33e932f6c6539d94/txt2img.py -O scripts/txt2img2.py
2.セーフフィルタ削除版で画像生成
画像生成スクリプトを通常のではtxt2img.pyなく、新たに保存したをtxt2img2.py指定して実行します。

以下は、セーフフィルタ削除版を使用した画像生成のコード例です：

# セーフフィルタを無効化して画像を生成
!python scripts/txt2img2.py \
    --plms \
    --ckpt ./Anything-V3.0-pruned.ckpt \
    --skip_grid \
    --n_samples 1 \
    --n_iter 1 \
    --outdir outputs \
    --ddim_steps 100 \
    --prompt "cute cat ear maid"
3. セーフフィルタ削除版を使う理由
通常版のスクリプト（txt2img.py）ではNSFW判定が適用され、一部の画像がフィルタリングされますが、このカスタムスクリプトではそのチェックがスキップされます。

注意事項
セーフフィルタを有効化すると、大事な内容が生成される可能性があります。使用目的や共有には十分に注意してください。
有効化スクリプトを実行する際も自己責任で行ってください。
これでセーフフィルタ削除版を使った画像生成が可能になります！












検索

推論

ChatGPT の回答は正しいとは限りません。重要な情報は確認してください。

?
