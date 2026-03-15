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
