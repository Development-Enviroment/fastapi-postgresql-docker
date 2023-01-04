# ディレクトリ構成
```
root/
 ├── .devcontainer/                             ・・・・リモートコンテナの設定
 ├── .github/
 │     └── PULL_REQUEST_TEMPLATE.md             ・・・・プルリクエストのテンプレート
 ├── docs/                                      ・・・・ドキュメント
 ├── src/                                       ・・・・ソースコード
 │    ├── app/                                  ・・・・アプリケーション
 │    │    ├── cruds/                           ・・・・CRUD処理する関数
 │    │    ├── models/                          ・・・・テーブル定義
 │    │    ├── routers/                         ・・・・APIのI/O(Swagger UI)
 │    │    └── schemas/                         ・・・・pydanticを用いたモデルスキーマ定義
 │    ├── lib/                                  ・・・・共通設定等のソースコード
 │    │    ├── models/
 │    │    ├── schemas/
 │    │    └── database.py                      ・・・・データベースのセッション
 │    ├── migrations/
 │    │    ├── versions/                        ・・・・マイグレーションスクリプトの管理
 │    │    │     └── XXXX_add_XXXX_table.py
 │    │    ├── README
 │    │    ├── env.py                           ・・・・migration実行用のスクリプト
 │    │    └── script.py.mako                   ・・・・migrationのスクリプトの生成用テンプレート
 │    ├── Dockerfile                            ・・・・ローカル環境用Dockerfile
 │    ├── Dockerfile.prod                       ・・・・本番環境用Dockerfile
 │    ├── alembic.ini                           ・・・・alembicの実行
 │    ├── main.py                               ・・・・エントリーポイント
 │    ├── requirements.txt                      ・・・・ライブラリの管理
 │    └── setup.cfg                             ・・・・formatterの設定
 ├── .gitignore                                 ・・・・GitHubにあげないファイルを指定
 ├── LICENSE
 ├── Makefile                                   ・・・・makeコマンドの設定
 ├── README.md
 ├── docker-compose.prod.yml                    ・・・・本番環境用docker-compose.yml
 ├── docker-compose.yaml                        ・・・・ローカル環境用docker-compose.yml
 └── env.example                                ・・・・環境変数

```