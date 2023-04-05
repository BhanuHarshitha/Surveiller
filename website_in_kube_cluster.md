```
version=$(curl -s "https://api.github.com/repos/kubernetes/ingress-nginx/releases" | grep tag_name | grep controller | sort -r | awk -F'"' 'NR==1 {print $4}'
```
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/${version}/deploy/static/provider/cloud/deploy.yaml
```
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048     -out self-signed-tls.crt      -keyout self-signed-tls.key      -subj "/CN=thewatcherpage.info/O=self-signed-tls"
```
```
kubectl create secret tls self-signed-tls --key self-signed-tls.key --cert self-signed-tls.crt
```
```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.11.0/cert-manager.yaml
```
`````
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kube-certs
  namespace: prod
spec:
  selector:
    matchLabels:
      app: kube-certs
  template:
    metadata:
      labels:
        app: kube-certs
    spec:
      terminationGracePeriodSeconds: 5
      containers:
      - name: server
        image: nitron181/the_watcher_repo:v2
        imagePullPolicy: Always
        ports:
        - containerPort: 8000
        env:
        - name: PORT
          value: "8000"
---
apiVersion: v1
kind: Service
metadata:
  name: kube-certs
  namespace: prod
spec:
  selector:
    app: kube-certs
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8000
  type: NodePort 
---
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: kubeissuer
  namespace: prod
spec:
  acme:
    # The ACME server URL
    server: https://acme-v02.api.letsencrypt.org/directory
    # Email address used for ACME registration
    email: ananthchaitanya17@gmail.com
    # Name of a secret used to store the ACME account private key
    privateKeySecretRef:
      name: kubeissuer
    # Enable the HTTP-01 challenge provider
    solvers:
    - http01:
        ingress:
          class: nginx          
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: kubecert
  namespace: prod
spec:
  secretName: demo
  issuerRef:
    name: kubeissuer
    kind: ClusterIssuer
  commonName: thewatcherpage.info
  dnsNames:
  - thewatcherpage.info
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    cert-manager.io/cluster-issuer: kubeissuer
    kubernetes.io/ingress.class: nginx
  name: kube-certs-ingress
  namespace: prod
spec:
  rules:
  - host: thewatcherpage.info
    http:
      paths:
      - backend:
          service:
            name: kube-certs
            port:
              number: 80
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - thewatcherpage.info
    secretName: demo
```