# コンテナ内でsqlコマンドを使用する時
### コンテナに入る
```
docker exec -it コンテナid /bin/bash
```
### コンテナ内でPostgreSQLの対話モードに入る
postgreSQLの対話モードに入るために、ルートユーザーを指定する。
```
psql -U postgres
```