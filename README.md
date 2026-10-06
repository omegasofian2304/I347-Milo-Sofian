# I347-Milo-Sofian

Web application with a FastAPI backend and a static frontend, fully containerized with Docker.

Built as part of the I347 module at CPNV.

## Project Structure

```
I347-Milo-Sofian/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile
├── frontend/
│   ├── index.html           # Web page
│   ├── script.js            # Fetches the API
│   └── Dockerfile
├── docker-compose.yaml
└── README.md
```

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (included with Docker Desktop)

## Getting Started

```bash
docker compose up --build
```

| Service  | URL                       |
|----------|---------------------------|
| Frontend | http://localhost:5500      |
| Backend  | http://localhost:8000      |

## Environment Variable

| Variable  | Description                              | Default Value |
|-----------|------------------------------------------|---------------|
| `MESSAGE` | Message displayed by the API and frontend | `Hello World` |

To customize the message:

```bash
# Linux / macOS
MESSAGE="Hello CPNV" docker compose up --build

# Windows PowerShell
$env:MESSAGE="Hello CPNV"; docker compose up --build
```

Or create a `.env` file at the project root:

```
MESSAGE=Hello CPNV
```

## API Endpoints

| Method | Route      | Description                              |
|--------|------------|------------------------------------------|
| GET    | `/`        | Returns a default message                |
| GET    | `/message` | Returns the value of `MESSAGE`           |

## Stopping

```bash
docker compose down
```

## Authors

- Milo Soupper
- Sofian Hussein
