# pythonのTags名を指定
FROM python:3.9.6-slim

# 処理を実行するフォルダ名を指定
WORKDIR /src

# copy src
COPY ./ /

# install system dependencies
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        libpq-dev\
        make \
        gcc

# 使用するライブラリのインストール
RUN pip install --upgrade pip
COPY ./src/requirements.txt /src/requirements.txt
RUN python3 -m pip install -r /src/requirements.txt

# マイグレーションに関するファイルのコピー
COPY ./src/migrations /src/migrations
COPY ./src/alembic.ini /src/alembic.ini

#初期データ用のSQO追加
# COPY ./src/lib/database/drop_table.sql /docker-entrypoint-initdb.d/
# RUN chmod 755 /docker-entrypoint-initdb.d/drop_table.sql
# COPY ./src/lib/database/insert_init_data.sql /docker-entrypoint-initdb.d/
# RUN chmod 755 /docker-entrypoint-initdb.d/insert_init_data.sql

# ------
RUN apt-get remove -y --purge make gcc build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# FastAPI起動コマンド
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
