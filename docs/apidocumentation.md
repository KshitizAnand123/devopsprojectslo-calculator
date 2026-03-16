# API Documentation

## Base URL

http://localhost:5000

---

## Endpoint

POST /calculate

---

## Request Parameters

| Parameter           | Type    | Description                       |
| ------------------- | ------- | --------------------------------- |
| total_requests      | integer | Total number of requests received |
| successful_requests | integer | Number of successful requests     |
| slo_target          | integer | Target reliability percentage     |

---

## Example Request

```
{
 "total_requests": 1000,
 "successful_requests": 995,
 "slo_target": 99
}
```

---

## Example Response

```
{
 "SLI": 99.5,
 "SLO Target": 99,
 "Status": "SLO Achieved"
}
```

---

## Status Meaning

SLO Achieved → Service reliability meets target
SLO Violated → Service reliability is below target

## Web Dashboard

In addition to the API endpoint, the project provides a simple web interface.

URL:

http://localhost:5000

The dashboard allows users to:

- Enter total requests
- Enter successful requests
- Enter SLO target

The dashboard sends the data to the `/calculate` API endpoint and displays the calculated SLI and SLO result.