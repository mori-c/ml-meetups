# Introduction

[ TOC ]
1. containers
2. scheduling
3. isolation
4. declarative state
5. resources
6. --
7. replica
8. service
9. deployment
10. resources
11. tools

---

* schedule containers
  * pull image in vm to run
  * env containers of various versions, like python
  * docker-swamp, K8s, Google Borg
* isolation
* declarative state as available resources
* small abstraction == pod (collection of containers, similar ideas and port IP space)
  * separate containers: data, web server, php
  * yaml / json format: 
```
apiVersion: v1
kind: pod/ReplicaSe
metadata:   // (of labelled resources as a construct)
  name: ngix
  labels: 
    app: webserver
spec: 
  replica: 3
  selector:
    matchLabels:
      app: webserver
  type: LoadBalancer / 
  template: 
    metadata:
    labels:
    app: webserver
    spec:
      containers: 
        images: nginx
        name: my-nginx
        ports: 
          containerPort: 80
      
```
* pod ssh: 
``` 
$ kubetctl apply -f nginx-pod.yml 
$ kubectl get pod
$ kubectl delete pod
$ kubecube delete all -l app=webserver
$ kubectl delete pod nginx-podName
$ kubectl apply -f nginx-service.yml
$ kubectl get svc                             // gets pod IP
$ kubeName ip                                 // expose cluster ID with localhost addy
$ kubectl apply -f nginx-deploy.yml           // deployment
```
* spec/type/LoadBalancer: services exposes to the outside world from the replica pods made
* deployment
 * new feature, bring pod with new image,
 * specs on deploying new pods
* resources:
  * config map
    * store secrets
    * ingress
    * volume: 
    * persistent volume claim in the clusters 
    * handle updates
    * loss
    * crash
    * node capacity, notification, add new pods to scale
* tools
  * minikube (takes lots of resources, 8gb)
  * kubectl                                                                  // kubernetes ssh
  * docker (helps to build images)
  * docker registry (push public images)
  * distributions: (more services & resources)
    * GKE (kub eng) / Google Cloud
    * EKS / AWS (elastic) 
    * AKS / Azure
    * Digital Ocean K8s
    * OpenShift
  * DIY
    * Kops ()
    * Kubespray
    * ShapeBlock


* https://slides.com/lakshminp/deck-5#/
* https://kompose.io                                           translate docker-compose files => kubernetes resources
* https://keel.sh                                                  ssh 
* https://github.com/openshift/source-to-image      S2I workflow toolkit to build source code reproducible Docker images


warning:
you are locked into framework as there are few translatable services to convert to other frameworks
recommend OpenShift