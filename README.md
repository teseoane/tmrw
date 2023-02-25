[![pipeline status](https://gitlab.com/mrmilu-team-dev/django.base/badges/master/pipeline.svg)](https://gitlab.com/mrmilu-team-dev/django.base/-/commits/master)
[![coverage report](https://gitlab.com/mrmilu-team-dev/django.base/badges/master/coverage.svg)](https://gitlab.com/mrmilu-team-dev/django.base/-/commits/master)

# project_name
Repository to project_name

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
python3 -m venv venv/project_name
source ./venv/project_name
pip install -r requirements/local.txt
pre-commit install
```

### Getting a django shell inside Docker container
```
docker compose -f local.yml run --rm django python manage.py shell_plus
```
