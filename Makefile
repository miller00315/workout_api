run:
	@uvicorn workout_api.main:app --reload

db:
	@docker compose up -d

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head