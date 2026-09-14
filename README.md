# Travel Decision Engine

A FastAPI backend for modelling potential trips, calculating travel costs under different assumptions, creating alternative scenarios, and comparing the financial trade-offs between travel options.

## 🚀 Project Vision

Travel planning information is often scattered across notes apps, spreadsheets, booking websites, and calculators.

Travel Decision Engine provides a structured way to model potential trips and understand the financial consequences of different choices. Users provide assumptions such as trip duration, traveller count, and estimated costs, while the engine calculates and compares the resulting trade-offs - leaving the final decision to the user.

## ✨ Planned Features

### Trip Modelling

* Create and manage trip ideas
* Store destination, trip duration, and traveller count

### Dynamic Cost Engine

* Add costs using one-off, per-day, and per-night pricing
* Support shared and per-person costs
* Calculate total, per-person, category, and individual cost breakdowns

### Scenarios

* Create alternative versions of a trip using lightweight overrides
* Change trip duration, traveller count, or exclude selected costs

### Comparison & Decision Support

* Compare scenarios and different trip options
* Show differences in duration, total cost, per-person cost, and cost categories
* Generate factual trade-off insights without subjective recommendations

## 🛠 Tech Stack

* Python 3.11
* FastAPI - REST API framework
* SQLModel - Database modelling
* SQLite - Database
* Pydantic - Data validation
* Pytest - Testing framework
* GitHub Actions - Continuous Integration (CI)
* Codecov - Test coverage reporting
* Mypy - Static type checking

## 🎯 V1 Scope

V1 focuses on building a working backend for modelling trips, calculating costs, creating alternative scenarios, and comparing travel options.

V1 will include:

* Trip and cost item management
* Dynamic cost calculations and breakdowns
* Lightweight trip scenarios using overrides
* Side-by-side comparison of evaluated options
* Factual insights highlighting key trade-offs
* Structured API responses through FastAPI

V1 will intentionally remain focused on backend logic and API design rather than frontend features or external integrations.

## ✅ Current Status

The core FastAPI foundation is complete, including:

* Full Trip CRUD API
* SQLModel and SQLite persistence
* Pydantic validation and 404 handling
* Isolated database testing with Pytest
* Modular models, schemas, services, routes, and tests
* GitHub Actions CI

Development is now moving into the V1 decision-engine features, starting with the updated Trip model and CostItem system.
