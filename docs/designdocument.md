# Design Document

## System Overview

The SLO/SLI Calculator evaluates service reliability using monitoring metrics.

The system accepts monitoring data such as total requests and successful requests and calculates the Service Level Indicator (SLI). The calculated SLI is compared with a predefined Service Level Objective (SLO).

---

## Architecture

User → REST API → SLI Calculation Logic → Response

---

## Components

### API Layer

Handles incoming HTTP requests.

### Business Logic

Calculates SLI values and evaluates SLO compliance.

### DevOps Infrastructure

Includes Docker containerization, CI/CD pipelines, monitoring configurations, and configuration management scripts.

---

## Deployment

The application runs as a containerized service using Docker and can be deployed using Docker Compose.

---

## Reliability Metric

SLI Calculation Formula:

SLI = (Successful Requests / Total Requests) × 100
