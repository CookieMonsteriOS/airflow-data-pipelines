# Use the official Airflow image
FROM apache/airflow:2.10.5

#Install postgres
RUN pip install apache-airflow-providers-amazon==6.2.0
RUN pip install apache-airflow-providers-postgres==2.3.0

# Switch to root user to install dependencies
USER root

# Update apt-get and install necessary dependencies
RUN apt-get update && \
    apt-get install -y build-essential libatlas-base-dev && \
    apt-get clean

# Switch back to the default airflow user
USER airflow

# Ensure the correct directories are created
RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins

# Set the Airflow UID to avoid permission issues
ENV AIRFLOW_UID=50000

# Default entrypoint is already defined in the base image, so no need to redefine it
# We will specify the default command for Airflow webserver (or any other component)
CMD ["webserver"]
