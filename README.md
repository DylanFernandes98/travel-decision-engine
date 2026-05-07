# Travel Decision Engine

A FastAPI backend for modelling travel plans, generating trip variants, and evaluating holidays using dynamic cost calculations and trip comparisons.

## 🚀 Project Vision

Travel planning information is often scattered across notes apps, spreadsheets, booking websites, and calculators.

Travel Decision Engine aims to provide a more structured way to model trips, explore variants, and evaluate travel trade-offs such as cost, duration, optional activities, and annual leave usage.

## ✨ Planned Features

### Trip Modelling
- Create and manage trip ideas
- Store destinations, trip duration, people count, and annual leave usage
- Support trip presets such as `hiking_trip`, `short_break`, and `bucket_list`
- Add notes and optional activities to trips

### Dynamic Cost Engine
- Support fixed, per-day, and per-person cost types
- Automatically calculate total trip cost and cost per person
- Recalculate costs dynamically when trip duration changes
- Model optional costs such as activities, transport, or trip extensions

### Trip Variant Engine
- Generate and compare variants of the same trip
- Compare combinations such as:
  - Monza + Switzerland
  - Switzerland only
  - Extended trip durations
- Include or remove optional trip legs and activities

### Comparison & Decision Support
- Compare completely different holiday options
- Evaluate trips using configurable comparison logic
- Analyse factors such as:
  - value for money
  - travel complexity
  - trip duration
  - hiking suitability
  - accommodation quality
- Generate recommendation summaries and trade-off insights

## 🛠 Planned Tech Stack

- Python 3
- FastAPI - REST API framework
- SQLModel - Database models and ORM layer
- SQLite - Initial database solution
- Pydantic - Data validation and schemas
- Pytest - Testing framework
- GitHub Actions - Continuous Integration (CI)
- Codecov - Test coverage reporting
- Mypy - Static type checking

## 🎯 V1 Scope

The first version of the project will focus on building a working backend for creating trip ideas, modelling costs, and comparing travel options.

V1 will include:

- Create and retrieve trip ideas
- Store basic trip details such as destination, duration, people count, and annual leave usage
- Add cost items to trips using different cost types
- Calculate total trip cost and cost per person
- Create simple trip variants by changing duration or optional costs
- Compare multiple trip options using core metrics
- Provide structured API responses through FastAPI

V1 will intentionally keep the scope focused on backend logic and API design rather than frontend features or external integrations.

## ❌ Out of Scope (Initially)

- Flight or accommodation scraping
- Live pricing integrations
- Frontend applications
- User authentication
- AI-generated itineraries
- External booking integrations
