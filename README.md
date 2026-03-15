# Local Cloud-Native Development Stack

This project demonstrates a fully integrated DevOps environment using Docker, Terraform, and LocalStack to simulate an AWS cloud environment locally.

## Architecture
- **Web App:** Flask (Python) API.
- **Database:** Redis for hit counting.
- **Cloud Storage:** LocalStack (S3) for persistent logging.
- **Infrastructure:** Managed via Terraform.

## How to Run
1. **Start the Stack:**
   ```bash
   docker compose up --build -d
