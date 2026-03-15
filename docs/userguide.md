# User Guide

## Running the Application

### Using Python

Navigate to the project folder and run:

```
python src/main/app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

### Using Docker

Build image:

```
docker build -t slo-calculator -f infrastructure/docker/Dockerfile .
```

Run container:

```
docker run -p 5000:5000 slo-calculator
```

---

## Using the API

Send a POST request to:

```
/calculate
```

Example request:

```
{
 "total_requests": 1000,
 "successful_requests": 995,
 "slo_target": 99
}
```

The API returns calculated SLI and whether the SLO target is achieved.
