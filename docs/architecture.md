# Project architecture overview

## Project Structure

```
src
└── app
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   └── v1
    │       ├── __init__.py
    │       ├── api.py
    │       └── endpoints
    │           ├── __init__.py
    │           └── webhook.py
    ├── components
    │   ├── __init__.py
    |   └── component # Each component has its own directory
    │       ├── __init__.py
    │       ├── handler.py
    │       └── schema.py
    ├── core
    │   ├── __init__.py
    │   ├── base_webhook_event_schema.py
    │   ├── config.py
    │   └── dependencies.py
    ├── main.py
    └── utils
        ├── __init__.py
        ├── load_submodules.py
        └── logger.py
```

## Project Overview

This project is a FastAPI-based API server with a structured directory layout. It provides various endpoints for handling webhooks and sensor data related to Zoom rooms.

The project is organized into the following main directories:

### 1. `api`

The `api` directory serves as the core of the api routes of the application and contains the API routers.

- `api`: Contains the API routers for different API versions.
- `api/v1`: Contains the API endpoints for version 1 of the API.

### 2. `components`

The `components` directory holds reusable components that are used by the API endpoints. Each component has its own handler and schema files.

- `endpoint_url_validation`: Contains the components for validating endpoint URLs.
- `zoom_room_checked_in`: Contains the components for handling checked-in Zoom room events.
- `zoom_room_checked_out`: Contains the components for handling checked-out Zoom room events.
- `zoom_room_sensor_data`: Contains the components for handling sensor data from Zoom rooms.

### 3. `core`

The `core` directory houses core functionalities and configurations of the application.

- `base_webhook_event_schema.py`: Defines the base schema for webhook events.
- `config.py`: Contains application configurations.
- `dependencies.py`: Contains dependencies required by the API endpoints.

### 4. `utils`

The `utils` directory contains utility files used throughout the application.

- `load_submodules.py`: A utility to load submodules dynamically.
- `logger.py`: Contains the logger configuration.

### 5. `main.py`

The `main.py` file is the entry point of the FastAPI application. It sets up the FastAPI app and includes the API routers from the `app` directory.

## Project Functionality

The project was developed to provide an API server for handling webhooks related to Zoom.
The way it has been implemented is that the API server receives the webhook events from Zoom and then processes them accordingly, using the components in the `components` directory.
All the `components` are loaded dynamically using the `load_submodules.py` utility.
