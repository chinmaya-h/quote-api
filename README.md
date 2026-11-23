# Quote API

A small REST API built with Java 17, Spring Boot, and Maven.

## Build and test

```bash
mvn clean package



## CI/CD & Deployment Architecture
- **CI Pipeline:** Jenkins (`pollSCM`) runs JUnit tests (`mvn test`), builds `target/quote-api.jar`, and archives the artifact.
- **Configuration Management:** Ansible playbook (`ansible/playbook.yml`) configures OpenJDK 17 and deploys the systemd service using a `common` role and restart handler.
- **Orchestration:** Kubernetes (`k8s-deployment.yaml`) runs 3 replicas on Minikube with `/health` Liveness and Readiness probes exposed via NodePort `30080`.
