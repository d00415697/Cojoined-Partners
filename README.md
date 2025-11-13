# **Predator Message Log**

## **Resource**
**Message**

### **Attributes**
- `name` (string) — Predator’s name  
- `description` (string) — Short description of the Predator  
- `age` (integer) — Predator’s age  
- `rank` (string) — Predator’s Yautja ranking  
- `kills` (integer) — Number of confirmed kills  

---

## **Schema**

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    age INTEGER,
    rank TEXT,
    kills INTEGER
);
```

## **REST Endpoints**

| **Name** | **Method** | **Path** | **Description** |
|-----------|-------------|----------|------------------|
| Retrieve message collection | GET | `/messages` | Returns all Predator records as JSON |
| Retrieve single message | GET | `/messages/<id>` | Returns a single Predator record by ID *(optional)* |
| Create message | POST | `/messages` | Adds a new Predator record |
| Update message | PUT | `/messages/<id>` | Updates an existing Predator record |
| Delete message | DELETE | `/messages/<id>` | Deletes a Predator record by ID |


## Building and Deploying

All of the following commands are to be run from the root of this repo

### Docker

Building the **client** image
```bash
docker build -t pacethomson/client_predator:lastest ./client/
```
Pushing the **client** image to DockerHub
```bash
docker push pacethomson/client_predator:lastest
```

---

Building the **server** container
```bash
docker build -t pacethomson/server_predator:lastest ./server/
```
Pushing the **server** image to DockerHub
```bash
docker push pacethomson/server_predator:lastest
```

### Kubernetes

Setting up the nginx-controller

1. **Install the NGINX Ingress Controller:**
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.1/deploy/static/provider/cloud/deploy.yaml
   ```

2. **Wait for the controller to be ready:**
   ```bash
   kubectl wait --namespace ingress-nginx \
     --for=condition=ready pod \
     --selector=app.kubernetes.io/component=controller \
     --timeout=90s
   ```

3. **Patch the service to use NodePort on port 80:**
   ```bash
   kubectl patch service ingress-nginx-controller -n ingress-nginx \
     -p '{"spec":{"type":"NodePort","ports":[{"port":80,"targetPort":80,"protocol":"TCP","name":"http","nodePort":30080},{"port":443,"targetPort":443,"protocol":"TCP","name":"https","nodePort":30443}]}}'
   ```

Applying our K8s files

Server Deployment, ClusterIP Service, and Persistent Volume Claim:
```bash
kubectl apply -f server/server-kube.yml
```

Client Deployment and Load Balancer:
```bash
kubectl apply -f client/client-kube.yml
```

Ingress:
```bash
kubectl apply -f ingress.yml
```



