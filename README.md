# EKS-DynamoDB-Deployment-Project


eksctl create cluster \
--name nikhil-cluster \
--region us-east-1 \
--vpc-public-subnets subnet-0329f1855d219a5bb,subnet-00837f69cbf2bcd41 \
--vpc-private-subnets subnet-0f8459b8c3bc14e8f,subnet-026faaf91561c7f3c \
--node-type t3.small \
--nodes 2 \
--node-private-networking \


kubectl get nodes 

Worker nodes → private subnet
Load balancer → public subnet

deployment.yaml
service.yaml

Service type: Loadbalncer
kubectl logs pod
kubectl exec -it pod -- bash
kubectl describe pod

CloudFront
   ↓
ALB
   ↓
EKS
   ↓
Pods
   ↓
DynamoDB

Name: nikhil-eks-vpc
CIDR: 10.0.0.0/16

public-subnet-1 ,public-subnet-2
10.0.1.0/24,10.0.2.0/24
AZ: us-east-1a

AZ: us-east-1b

private-subnet-1 ,private-subnet-2
10.0.3.0/24,10.0.4.0/24


AZ: us-east-1bInside VPC → Internet Gateway

NAT Gateway in public-subnet-1  assign elasitic ip
0.0.0.0/0 → Internet Gateway -->public-subnet-1   public-subnet-2

ag public subnets:

Key: kubernetes.io/role/elb
Value: 1

Tag private subnets:

Key: kubernetes.io/role/internal-elb
Value: 1

These tags allow
Elastic Load Balancing to work with EKS.
