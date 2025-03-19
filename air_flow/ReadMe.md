# Airflow Project

This project is an Apache Airflow setup for managing and scheduling workflows. It includes configurations for running Airflow with Docker Compose and supports integration with PostgreSQL and S3.

## Features

- Workflow orchestration with Apache Airflow.
- PostgreSQL as the metadata database.
- S3 integration for storage.
- Docker Compose setup for easy deployment.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.11 (if running Airflow locally).

## Setup Instructions

### Using Docker Compose

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Build and start the services: docker-compose up -d

3. Initialize the Airflow database: docker-compose run airflow-init

4. Access the Airflow web interface at http://localhost:8080.

Running Locally (Optional)

1. Create a Python virtual environment:

python3 -m venv py_env
source py_env/bin/activate

2. Install Airflow:

pip install apache-airflow

3. Initialize the Airflow database:

airflow db init

4. Start the Airflow webserver and scheduler:

airflow webserver --port 8080
airflow scheduler

## Environment variables

AIRFLOW_HOME: Path to the Airflow home directory.

AIRFLOW_UID: User ID for running Airflow in 

Docker <vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>. </vscode_annotation>- AWS_ACCESS_KEY_ID: 

## Access key for S3 integration.

AWS_SECRET_ACCESS_KEY: Secret key for S3 integration.

S3_ENDPOINT_URL: URL for the S3 endpoint.


License
This project is licensed under the MIT License.

You can copy and paste this content into your [README.md](http://_vscodecontentref_/2) file. It combines all the necessary information, including setup instructions, environment variables, and the [.gitignore](http://_vscodecontentref_/3) configuration, into one cohesive document.
