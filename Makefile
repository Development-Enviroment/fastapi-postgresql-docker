.PHONY: build-local
build-local: # コンテナ起動&ビルド
	@echo ビルド中...
	docker-compose up --build -d
	@echo ビルドを終了し,コンテナを起動しました

.PHONY: up
up: # コンテナ起動
	@echo コンテナを起動中...
	docker-compose up -d
	@echo コンテナを起動しました

.PHONY: up-log
up-log: # コンテナ起動(log見たい時)
	docker-compose up

.PHONY: down
down: # コンテナ停止
	docker-compose down
	@echo コンテナを停止しました

.PHONY: ps
ps: # コンテナの確認
	docker ps

.PHONY: generate-migration
generate-migration: # マイグレーションファイル生成
	docker-compose exec api alembic revision --autogenerate
	@echo マイグレーションファイルを生成しました

.PHONY: migrate
migrate: # マイグレーションの内容をdbに反映
	docker-compose exec api alembic upgrade head
	@echo テーブルを作成しました

.PHONY: formatter
formatter: # flake8, mypy, isortの検査
	@echo 確認中...
	docker-compose exec api flake8 .
	docker-compose exec api mypy .
	docker-compose exec api isort .
	@echo 完了