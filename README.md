# FastAPI Final Calculator

A robust, full-stack calculator application featuring user authentication and complete BREAD (Browse, Read, Edit, Add, Delete) operations. Built with FastAPI and dynamically rendered Jinja2 templates, this project utilizes a fully automated DevSecOps CI/CD pipeline with Pytest, Playwright UI testing, and Trivy container security scanning.

## 🔗 Live Docker Hub Repository
**Docker Image:** [reyesfrancisp/final_calculator](https://hub.docker.com/repositories/reyesfrancisp)

---

## 🛠️ Tech Stack
* **Backend:** FastAPI, Python 3.10
* **Database:** PostgreSQL (via SQLAlchemy ORM)
* **Frontend:** HTML, TailwindCSS, Vanilla JS, Jinja2 Templates
* **Security:** JWT Authentication, bcrypt password hashing
* **Testing:** Pytest (Unit/Integration), Playwright (E2E UI)
* **DevOps:** Docker, Docker Compose, GitHub Actions, Trivy

---

## 🐳 How to Run the Application Locally

This application is fully containerized. You do not need to install Python or PostgreSQL locally, only Docker and Git.

**1. Clone the repository:**
```bash
git clone [https://github.com/Reyesfrancisp/final-calculator.git](https://github.com/Reyesfrancisp/final-calculator.git)
cd final-calculator
```

**2. Build and start the containers:**
```bash
docker-compose up -d --build
```

**3. Access the Application:**
* **Frontend UI:** Open your browser and navigate to [http://localhost:8000](http://localhost:8000)
* **Interactive API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **API Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

**4. Stop the application:**
```bash
docker-compose down
```

---

## 🧪 How to Execute Tests Locally

The test suite (including the Playwright End-to-End UI tests) must be executed *inside* the running Docker container, as it requires access to the internal database network.

**1. Ensure your containers are running:**
```bash
docker-compose up -d
```

**2. Run the entire test suite (Unit, Integration, and E2E):**
```bash
docker-compose exec web pytest -v
```

**3. Run ONLY the Playwright UI Tests (BREAD Operations):**
```bash
docker-compose exec web pytest tests/e2e/test_bread_ui.py -v
```

**4. View Test Coverage:**
```bash
docker-compose exec web pytest --cov=app --cov-report=term-missing
```

---

## 🔐 Security & CI/CD Pipeline

This repository features a fully automated GitHub Actions workflow (`CI/CD`) that triggers on pushes to the `main` branch. The pipeline:
1. Provisions a temporary PostgreSQL database.
2. Installs dependencies and Playwright Linux binaries.
3. Executes the full Pytest suite.
4. Builds the Docker Image.
5. Scans the image for vulnerabilities using **AquaSecurity Trivy**. (Note: Unpatchable transitive dependency conflicts, such as those related to `pyasn1`, are explicitly managed via a `.trivyignore` file).
6. Automatically pushes the verified, passing image to Docker Hub.