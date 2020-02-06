.PHONY: test
test:
	docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm server

.PHONY: serve
serve:
	docker-compose -f docker-compose.yml up server

.PHONY: stop
stop:
	docker-compose -f docker-compose.yml -f docker-compose.test.yml down
