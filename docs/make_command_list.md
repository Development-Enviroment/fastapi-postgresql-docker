# makeコマンド一覧
### コンテナの起動&ビルド
```
make build-local
```
### コンテナ起動
```
make up
```
### コンテナ起動(log見たい時)
```
make up-log
```
### コンテナ停止
```
make down
```
### マイグレーションファイル生成
```
make generate-migration
```
### マイグレーションの内容をdbに反映
```
make migrate
```
### flake8, mypy, isortの検査
```
make formatter
```