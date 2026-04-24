# flask server is running in oracle vm production
test:
	pytest

lint:
	flake8 .
	black .

deploy:
	scp -r . user@vm:/app

restart:
	ssh user@vm "sudo systemctl restart flask-app"
