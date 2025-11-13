# NGINX Ingress Controller Setup Guide

This guide will help you install the NGINX Ingress Controller and expose it via NodePort so your app is accessible from outside the network.

## Installation Steps

### Option 1: Using kubectl (Recommended for simplicity)

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

### Option 2: Using Helm (if you have Helm installed)

1. **Add the ingress-nginx Helm repository:**
   ```bash
   helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
   helm repo update
   ```

2. **Install with NodePort configuration:**
   ```bash
   helm install ingress-nginx ingress-nginx/ingress-nginx \
     --namespace ingress-nginx \
     --create-namespace \
     --set controller.service.type=NodePort \
     --set controller.service.nodePorts.http=30080 \
     --set controller.service.nodePorts.https=30443
   ```

## Verify Installation

1. **Check that the ingress controller pods are running:**
   ```bash
   kubectl get pods -n ingress-nginx
   ```

2. **Check the service and note the NodePort:**
   ```bash
   kubectl get svc -n ingress-nginx
   ```

3. **Get your node's external IP:**
   ```bash
   kubectl get nodes -o wide
   ```

## Access Your Application

Once everything is set up, you can access your application at:
- **Client (frontend):** `http://<your-server-ip>:30080/`
- **Server (API):** `http://<your-server-ip>:30080/messages`

Replace `<your-server-ip>` with the IP address of your Kubernetes node.

## Deployment Order

1. Install NGINX Ingress Controller (steps above)
2. Deploy your application:
   ```bash
   kubectl apply -f server/server-kube.yml
   kubectl apply -f client/client-kube.yml
   kubectl apply -f ingress.yml
   ```

## Troubleshooting

- If the ingress controller doesn't start, check logs:
  ```bash
  kubectl logs -n ingress-nginx -l app.kubernetes.io/component=controller
  ```

- Check if your Ingress resource is recognized:
  ```bash
  kubectl describe ingress app-ingress
  ```

- Verify services are running:
  ```bash
  kubectl get svc
  kubectl get pods
  ```

