docker images bpradipt/perf-sidecar-injector-amd64 -q | xargs -r docker rmi -f
make image
make release
kubectl delete -f deployment/deployment.yaml
sleep 6
kubectl apply -f deployment/deployment.yaml
cd ~/MasterThesis/main-test/calico-test/sidecar/k8s-sidecar-injector/examples/kubernetes
kubectl delete -f debug-pod.yaml
sleep 10
kubectl apply -f debug-pod.yaml

