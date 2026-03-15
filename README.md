# SLO / SLI Calculator

Student Name: Kshitiz Anand
Registration No: 23FE10CSE00773
Course: CSE3253 DevOps [PE6]
Semester: VI (2025–2026)
Project Type: Puppet/Monitoring
Difficulty: Intermediate

---

# Project Overview

## Problem Statement

Modern cloud services rely on reliability metrics such as Service Level Indicators (SLIs) and Service Level Objectives (SLOs). Monitoring systems collect metrics like request success rates, but teams need tools to evaluate whether the system meets its reliability targets.

This project implements a simple service that calculates SLI values based on monitoring data and compares them with defined SLO targets.

---

## Objectives

* Calculate SLI from service metrics
* Compare calculated SLI with SLO targets
* Demonstrate containerized deployment using Docker
* Demonstrate DevOps practices such as CI/CD, monitoring configuration, and infrastructure automation

---

## Key Features

* REST API for SLI/SLO evaluation
* Docker containerization
* CI/CD pipeline with GitHub Actions
* Monitoring configuration using Nagios
* Configuration management using Puppet

---

# Technology Stack

## Core Technologies

Programming Language: Python
Framework: Flask
Database: None

## DevOps Tools

Version Control: Git
CI/CD: GitHub Actions
Containerization: Docker
Orchestration: Docker Compose
Configuration Management: Puppet
Monitoring: Nagios

---

# Getting Started

## Prerequisites

* Docker Desktop
* Git
* Python 3.8+

---

## Installation

Clone the repository:

```
git clone https://github.com/KshitizAnand123/devopsprojectslo-calculator.git
cd devopsprojectslo-calculator
```

Run the application:

```
python src/main/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# Docker Usage

Build the Docker image:

```
docker build -t slo-calculator -f infrastructure/docker/Dockerfile .
```

Run container:

```
docker run -p 5000:5000 slo-calculator
```

---

# API Endpoint

POST `/calculate`

Example request:

```
{
 "total_requests": 1000,
 "successful_requests": 995,
 "slo_target": 99
}
```

Example response:

```
{
 "SLI": 99.5,
 "SLO Target": 99,
 "Status": "SLO Achieved"
}
```

---

# Project Structure

```
src/                Application source code
docs/               Project documentation
infrastructure/     Docker and Puppet configs
monitoring/         Monitoring configuration
pipelines/          CI/CD pipelines
tests/              Test files
```

---

# Author

Kshitiz Anand
