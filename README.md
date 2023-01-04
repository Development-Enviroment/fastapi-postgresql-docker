# FastAPI + PostgreSQL + Docker

## 1. 必須環境
- git
- docker


## 2. 環境構築
### 2-1. `.env`ファイルの作成
root に`.env`ファイルを作成し、↓ をコピペする。
```
DB_HOST="db"
DB_PORT="5432"
DB_NAME="postgres"
DB_USER="postgres"
DB_PASSWORD="postgres"
```
### 2-2. コンテナのビルド
```
make build-local
```
### 2-3. コンテナ起動
```
make up
```
ログを見ながら作業したい時は↓
```
make up-log
```
Swagger UI : http://127.0.0.1:8000/docs
### 2-4. コンテナ停止
```
make down
```


## 3. DBマイグレーション
### 3-1. マイグレーションファイル生成(これは基本的にやらないでいい)
```
make generate-migration
```
### 3-2. マイグレーションファイルの内容をDBに反映
```
make migrate
```


## 4. 開発ルール
### 4-1. ブランチ名
ローカル環境 : feat/hogehoge
### 4-2. コードフォーマット
事前に↓のコマンドで静的検査をし、全てのエラー・警告を消しておく。\
チェックが通らない場合は修正してからpushして下さい。
```
make formatter
```
> flake8
>
> コードスタイル検査(PEP8)、コメントアウトスタイル検査(PEP257)、論理エラー検査(PyFlakes)、複雑性検査(mccabe)

> mypy
>
> 型ヒント検査(PEP484)

> isort
>
> import 文の自動補正(PEP8)


## 5. Tips
- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [ディレクトリ構成](docs/directory_architecture.md)
- [makeコマンド一覧](docs/make_command_list.md)
- [pep8エラーコードチートシート](https://qiita.com/KuruwiC/items/8e12704e338e532eb34a)
- [コンテナ内でsqlコマンドを使用する時](docs/sql_in_container.md)