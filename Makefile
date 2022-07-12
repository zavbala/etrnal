build:
	docker compose up -d

clear:
	docker compose down
	docker rmi -f eternal_api eternal_client