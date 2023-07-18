# Fast API Zoom Webhook handler

[![Python tests](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/python-tests.yml/badge.svg)](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/python-tests.yml)
[![pre-commit](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/pre-commit.yaml)
[![CodeQL](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/SamuelGuillemet/zoom-python-webhook/branch/main/graph/badge.svg)](https://codecov.io/gh/SamuelGuillemet/zoom-python-webhook)
[![Deploy](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/build.yml/badge.svg)](https://github.com/SamuelGuillemet/zoom-python-webhook/actions/workflows/build.yml)

This is a simple FastAPI app that handles Zoom Webhooks.

The goal of this app is to provide a simple way to handle Zoom Webhooks and to provide a simple way to extend the app with custom handlers.

## Installation

```bash
$ git clone https://github.com/SamuelGuillemet/zoom-python-webhook.git
```

## Requirements

- Python >= 3.11
- Poetry

## How to configure the environment variables

### Defining your env variables

If your are in development mode, you can define the following variables in your `.env.development` file:

- `ZOOM_WEBHOOK_SECRET_TOKEN` : The secret token that you have defined in your Zoom App.

### Defining your env variables in production

If your are in production mode, you can define the following variables in your `.env.production` file or directly in your environment variables:

- `ZOOM_WEBHOOK_SECRET_TOKEN` : The secret token that you have defined in your Zoom App.

## Usage

### Production

There is a Dockerfile that you can use to build the image and run the app.

```bash
$ docker compose up -d --build
```

### Development

#### Install dependencies and run the project

Poetry will take all the information on the `pyproject.toml` file and will install all its dependencoies.

You can install Poetry using the following command:

**Linux or Mac:**

```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

**Windows:**

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Source: https://python-poetry.org/docs/#installing-with-the-official-installer

Then, you can install the dependencies with the following command:

#### Virtual env if you use Conda

Start the conda env:

```bash
$ conda activate your_env
```

Create a virtual env under the `.venv` folder:

```bash
$ python -m venv .venv
```

Deactivate the conda env:

```bash
$ conda deactivate
```

#### Install the dependencies

```bash
$ poetry install
```

Activate the virtual env:

```bash
$ source .venv/bin/activate
```

#### Install the pre-commit Git hook

```bash
$ pre-commit install
```

#### Run the app

Then, you can run the app with the following command from the root folder:

```bash
$ uvicorn src.app.main:app --reload --reload-dir=./src/app
```

## Supported events

- `endpoint.url_verification`
- `zoomroom.checked_in`
- `zoomroom.checked_out`

## How to add a new handler

1. Create a new component in the `src/app/components` folder.
2. The structure of the component should be the following:

```bash
├── your_component
│         ├── __init__.py
│         ├── handler.py
│         └── schema.py
```

3. In the `handler.py` file, you should create a new function that will handle the event. The function should be take the following arguments:
   - body (dict): The body of the request
4. In the `schema.py` file, you should create 2 new Pydantic models that will be used to validate the body of the request and the response of the handler function.
   - The first model should be used to validate the body of the request.
   - The second model should be used to validate the response of the handler function.
5. In the `__init__.py` file, you must have the following code:

```python
from .handler import your_handler_function
from .schema import YourResponseSchema

event_name = "your.event.name"
handler_function = your_handler_function
response_model = YourResponseSchema
```

6. All the components arle loaded dynamically in the `src/app/api/v1/endpoints/webhook.py` file.
