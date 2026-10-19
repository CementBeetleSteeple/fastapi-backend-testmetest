# fastapi-backend-testmetest

FastAPI microservice deployed on AWS ECS Fargate.

## Stack
- FastAPI + Uvicorn
- PostgreSQL (async via asyncpg)
- JWT auth
- AWS ECS Fargate + ECR
- GitHub Actions CI/CD

## Architecture

```
GitHub Actions CI/CD → ECR → ECS Fargate → RDS PostgreSQL
```
