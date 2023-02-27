# tmrw
Repository to tmrw

## Urls out of the box
- `/__status__` -> Health checks
- `/api/` -> Rest Framework base endpoints. Login required
- `/api/docs` -> API documentation. Login required
- `/auth-token` -> Get a valid API token
- `/api/schema` -> Open API schema

## Development

NOTE: The following command makes the assumption that you are using `docker conpose` version `>2`. if you are using a older version, please replace `docker compose` with `docker-compose`

### Running local environment
```bash
docker compose -f local.yml up
```

### Create superuser
In order to use some feature thar requires authentication like `admin` or some API endpoint you need a user with enough permmission. Just create one:
```bash
docker compose -f local.yml run --rm django python manage.py createsuperuser
```

### Creating and running migrations
```bash
docker compose -f local.yml run --rm django python manage.py makemigrations
docker compose -f local.yml run --rm django python manage.py migrate
```

### Running the tests
```bash
docker compose -f local.yml run --rm django python -m pytest
```

### Showing tests coverage
First run test with coverage to collect information
```bash
docker compose -f local.yml run --rm django coverage run -m pytest
```

To see a summary
```bash
docker compose -f local.yml run --rm django coverage report
```

or if you want to generete a complete html report you can type:
```bash
docker compose -f local.yml run --rm django coverage html
```

### Install pre-commit locally

```bash
python3 -m venv venv/tmrw
source ./venv/tmrw
pip install -r requirements/local.txt
pre-commit install
```

### Getting a django shell inside Docker container
```
docker compose -f local.yml run --rm django python manage.py shell_plus
```

## Notes:

- Since the priority management method is not specified, I opted for the fastest solution.
- Use celery with a single worker with 3 queues based on round-robin strategy.
- This allows a way to scale the solution by adding more workers.
- The project has a 100% of coverage.
- It only remains to make the notifications, which could be done with channels or websockets.

### Development process:

- I started by initializing a base project.
- Creation of a profile for the user to add the information of the priorities.
- Adds Job and JobSubmission models.
- Adds job list view.
- Adds job submission view set.
- Adds celery and redis.
- Adds celery priority queues.
- Adds service with method to proccess a job
- Adds task to call process
- Adds logging for task
