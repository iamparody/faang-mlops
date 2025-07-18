run:
	docker-compose up --build

monitor:
	docker-compose exec monitoring-service python monitor.py run

init-db:
	docker-compose exec monitoring-service python monitor.py init-db
