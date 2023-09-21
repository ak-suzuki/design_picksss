# Pythonのイメージ指定
FROM python:3.9
# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1
# コンテナのワークディレクトリを/var/www/に指定
WORKDIR /var/www/
# ローカルのrequirements.txtをコンテナの/var/www/フォルダ直下に置く
COPY requirements.txt /var/www/
# コンテナ内でpipをアップグレードした後、pip install -r requirements.txtを実行
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# ソースコードをコンテナにコピー
COPY . /var/www/
