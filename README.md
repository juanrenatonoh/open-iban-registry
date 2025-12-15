# 🌍 Open IBAN Registry API

[![Status: Educational / Portfolio Project](https://img.shields.io/badge/status-educational-blue)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green)]()

## 📌 Introduction

The **IBAN Registry** is an official dataset maintained by **SWIFT** under the **ISO 13616** standard. It defines the structure, length, and validation rules for International Bank Account Numbers (IBAN) across participating countries.

This project exposes the IBAN Registry as a **REST API**, allowing you to load the official registry file, persist it in **MongoDB**, and query it programmatically for validation, analysis, and integration purposes.

---

## 🎯 Project Purpose

This repository started as a simple script to transform the IBAN registry TXT file into Excel. It has evolved into a **backend API** designed for:

- Loading the official IBAN Registry file
- Persisting normalized data into MongoDB
- Querying IBAN, BBAN, and country metadata via HTTP endpoints

The project is intentionally kept **non-production** and oriented toward **learning, experimentation, and portfolio demonstration**.

---

## 🧠 Educational Disclaimer

> ⚠️ **Important Notice**
>
> This project is developed **exclusively for educational, research, and portfolio purposes**.
>
> - It is **not intended for production use**
> - It does **not provide financial or banking services**
> - It is **not affiliated with SWIFT or any financial institution**
>
> All data used comes from **publicly available SWIFT documentation**. Use this project at your own discretion.

---

## 🛠️ Technologies Used

Based on the current `pyproject.toml`, the project uses the following technologies:

### Core
- **Python 3.11+**
- **FastAPI** – REST API framework
- **Pydantic v2** – Data validation and modeling
- **Pydantic Settings** – Environment-based configuration

### Data Processing
- **Pandas** – Data parsing and transformation
- **OpenPyXL** – Excel handling (legacy and analysis support)

### Persistence
- **MongoDB**
- **PyMongo** – MongoDB driver

### Infrastructure & Tooling
- **Docker** – Containerized execution
- **Docker Compose** – Dev and test environments
- **GHCR (GitHub Container Registry)** – Image distribution

---

## 🐳 Running the API (Test Mode)

A prebuilt Docker image is available for testing purposes.

### Image
```
ghcr.io/juanrenatonoh/iban-registry:latest
```

### Environment Configuration

```bash
cp .env.example .env.test
```

### Using docker-compose (test)

```bash
docker compose -f docker-compose.test.yml up
```

This mode is intended for:
- API exploration
- Contract testing
- Local experimentation

---

## 💻 Development Mode

For local development, use the dedicated development compose file.

### Environment Configuration

```bash
cp .env.example .env.dev
```

### Using docker-compose (dev)

```bash
docker compose -f docker-compose.dev.yml up
```

Adjust values as needed (MongoDB connection, ports, etc.).

---

## 📂 Repository Structure (High Level)

```
open-iban-registry/
├── app/                # FastAPI application
├── docker-compose.dev.yml
├── docker-compose.test.yml
├── Dockerfile
├── pyproject.toml
├── .env.example
└── README.md
```

---

## 📚 Data Source & References

- **ISO 13616** – International standard for IBAN
- **SWIFT IBAN Registry** – Official public documentation

This project **does not redistribute proprietary services**, it only processes publicly available registry data.

---

## 🔌 API Access & Registry Loading

This project exposes the IBAN Registry through a **REST API built with FastAPI**.  
A **temporary public deployment** is available for testing and demonstration purposes.

---

### 🌐 Live API (Temporary – Render)

The API is currently deployed on **Render** and is intended **only for testing and portfolio demonstration**.

**Base URL**

https://iban-registry-latest.onrender.com


**OpenAPI Specification**

https://iban-registry-latest.onrender.com/openapi.json


**Swagger UI**

https://iban-registry-latest.onrender.com/docs


> ⚠️ **Important**  
> This deployment is **temporary**.  
> Availability, data persistence, and performance are **not guaranteed**.  
> The service may be restarted, limited, or removed at any time.

---

### 📥 IBAN Registry TXT File

To load data into the API, the official **IBAN Registry TXT file** is required.

You can obtain it from the following sources:

#### 🏛️ Official Source (Recommended)
Maintained by **SWIFT**, the authoritative source of the IBAN Registry:

https://www.swift.com/swift-resource/11971/download


#### 📁 Repository Version (Convenience)
A versioned copy is included in this repository for reproducibility and testing:

https://github.com/juanrenatonoh/open-iban-registry/blob/main/docs/iban-registry.txt


> ℹ️ The IBAN Registry data is publicly available and owned by **SWIFT**.  
> This project only processes the data and does not claim ownership.

---

### 📘 Available API Endpoints

Below is a high-level overview of the main API endpoints exposed by the service.

| Method | Endpoint                         | Description |
|------:|----------------------------------|-------------|
| GET   | `/health`                        | Health check endpoint |
| POST  | `/registry/upload`               | Loads and parses the IBAN registry TXT file into MongoDB |
| GET   | `/registry/`                     | Get record from Iban Registry |
| GET   | `/openapi.json`                  | OpenAPI specification |
| GET   | `/docs`                          | Interactive Swagger UI |

> Endpoint structure and responses may evolve as the project matures.

---

### 🚧 Usage Notes & Limitations

- No authentication or authorization
- No rate limiting
- No SLA or uptime guarantees
- Not suitable for production or financial operations

This API is designed strictly for **educational, research, and portfolio use**.

## 👤 Author & Portfolio

**Juan Renato Noh**  
Software Engineer | Backend | APIs

- 💼 LinkedIn: https://www.linkedin.com/in/juanrenatonoh/
- 🌐 Blog: https://juanrenatonoh.blogspot.com/

This repository is part of my **professional portfolio**.

---

## ❤️ Dedication

This project is lovingly dedicated to my sons:

**Matí & Emi** 👨‍👦‍👦

You are my greatest motivation to keep learning, building, and sharing knowledge.

---

## 📄 License

This project is licensed under the **MIT License**.

> The IBAN Registry data belongs to **SWIFT** and remains subject to their respective terms and conditions.

---

*I have no special talents. I am only passionately.* 🚀
