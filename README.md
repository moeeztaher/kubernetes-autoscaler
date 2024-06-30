# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

# install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# install helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh


# start minikube
minikube start


# enable metrics server
minikube addons enable metrics-server


# deploy the app to minikube according to settings in app-deployment.yaml
kubectl apply -f app-deployment.yaml


# open minikube dashboard
minikube dashboard


# enable ingress in minikube
minikube addons enable ingress


# list ingress pods
kubectl get pods -n ingress-nginx


# expose the web app deployment via a service of type NodePort
kubectl expose deployment classifier-api --type=NodePort --port=8000

# gives a public ip to access the service
minikube service classifier-api --url

# create ingress object, uses nginx, routes traffic to the service
kubectl apply -f app-ingress.yaml

# list ingress objects
kubectl get ingress

# get details for ingress
kubectl describe ingress


# enable HPA
kubectl autoscale deployment classifier-api --cpu-percent=50 --min=1 --max=10
or
kubectl apply -f app-hpa.yaml

# load test
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://test.example; done"

# watch the cpu utilization in the HPA
kubectl get hpa classifier-api --watch



# get yaml for an object
kubectl get service classifier-api -o yaml --> app-service.yaml



# install prometheus
helm install prometheus prometheus-community/prometheus

# expose prometheus service
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-np

# get prometheus pods
kubectl get pods -l app.kubernetes.io/instance=prometheus

# open prometheus dashboard
minikube service prometheus-server-np

