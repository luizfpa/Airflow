# Airflow Project by luizfpa

## Overview
This repository, maintained by `luizfpa`, is a practice implementation of [Apache Airflow](https://airflow.apache.org/), a platform to programmatically author, schedule, and monitor workflows. This project is designed to practice exercises from the LinkedIn Learning course [Learning Apache Airflow](https://www.linkedin.com/learning/learning-apache-airflow/an-overview-of-apache-airflow?u=264700066).

## Table of Contents
- [Project Focus](#project-focus)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Project Focus
This Airflow project is designed to practice creating and managing data pipelines through exercises from the LinkedIn Learning course "Learning Apache Airflow." It focuses on building simple Directed Acyclic Graphs (DAGs) to process data stored in the `datasets` folder, with outputs saved to the `output` folder after DAG execution. The repository is intended for beginners to learn Airflow concepts, such as task dependencies, scheduling, and workflow management, in a simple and hands-on manner.

## Features
- **Simple DAGs**: Define basic workflows as Directed Acyclic Graphs (DAGs) using Python code, following course exercises.
- **Local Data Processing**: Process data from the `datasets` folder and save results to the `output` folder.
- **Learning-Oriented**: Includes example DAGs to practice core Airflow concepts like task dependencies and scheduling.
- **Monitoring**: Use Airflow’s web UI to visualize DAG execution and troubleshoot issues.

## Getting Started
To get started with this Airflow project, follow these steps to set up a local environment.

### Prerequisites
- Python 3.9, 3.10, 3.11, or 3.12
- PostgreSQL, MySQL, or SQLite (for development; SQLite not recommended for production)
- Docker (optional, for containerized setup)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/luizfpa/Airflow.git
   cd Airflow
   ```

2. **Install Airflow via PyPI**:
   Use the following command to install Airflow with constraints for a repeatable installation:
   ```bash
   pip install 'apache-airflow==3.0.3' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.3/constraints-3.10.txt"
   ```

3. **Optional: Install with Extras** (e.g., for PostgreSQL):
   ```bash
   pip install 'apache-airflow[postgres]==3.0.3' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.3/constraints-3.10.txt"
   ```

4. **Initialize the Database**:
   ```bash
   airflow db init
   ```

5. **Start Airflow Standalone** (for testing):
   ```bash
   airflow standalone
   ```
   Access the Airflow UI at `localhost:8080` (default credentials: `airflow`/`airflow`).

6. **Docker Setup** (alternative):
   Download the official Airflow `docker-compose.yaml`:
   ```bash
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.0.3/docker-compose.yaml'
   ```
   Initialize and start:
   ```bash
   docker compose up airflow-init
   docker compose up
   ```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please review the [CONTRIBUTING.rst](CONTRIBUTING.rst) file for detailed guidelines.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
