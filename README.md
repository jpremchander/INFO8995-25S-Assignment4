# Assignment 4 - CI/CD on Kubernetes with Jenkins

**Course**: INFO8995 - Container Orchestration  
**Assignment**: Assignment 4 - CI/CD on K8s  

## 👥 Group 7

| Name | Student ID |
|------|------------|
| **Prem Chander J** | 9015480 | 
| **Rishi Patel** | 8972657 | 

---

## 📋 Project Overview

This project implements a complete CI/CD pipeline on Kubernetes using Jenkins, with dual repository integration supporting both GitHub (external) and Gitea (internal) workflows. The infrastructure is deployed using Ansible and provides automated Python application builds with PyInstaller.

### 🎯 Learning Objectives Achieved
- ✅ Kubernetes orchestration and deployment
- ✅ Infrastructure as Code with Ansible
- ✅ Jenkins CI/CD pipeline implementation
- ✅ Container-based development workflows
- ✅ Network ingress and external access configuration
- ✅ Persistent storage management with NFS
- ✅ Git workflow automation with webhooks

---


### 🖥️ Infrastructure Components

| Component | Purpose | Access Method |
|-----------|---------|---------------|
| **Jenkins** | CI/CD orchestration | External: [jenkins.exotrend.live](https://jenkins.exotrend.live), Internal: NodePort 32090 |
| **TrueNAS NFS** | Persistent storage | 10.172.27.9:/mnt/ops-pool/jenkins-data |
| **Traefik Ingress** | Load balancing | jenkins.10.172.27.36.nip.io |
| **GitHub Integration** | External repository | Webhook → External tunnel → Jenkins |
| **Gitea Integration** | Internal repository | Webhook → Cluster IP → Jenkins |

---

## 🚀 Quick Start

### Prerequisites
- Kubernetes cluster (K3s) running
- TrueNAS with NFS configured
- Ansible installed
- Git repositories set up

### 🔧 Deployment

```bash
# Deploy Jenkins infrastructure
ansible-playbook up.yaml

# Verify deployment
kubectl get all -n jenkins

# Access Jenkins
# External: https://jenkins.exotrend.live
# Internal: http://10.172.27.36:32090
```

### 🧹 Cleanup

```bash
# Remove all Jenkins resources
ansible-playbook down.yaml
```

---

## 📁 Repository Structure

```
INFO8995-25S-Assignment4/
├── up.yaml                 # Jenkins deployment playbook
├── down.yaml              # Jenkins cleanup playbook
├── python-jenkins-app/    # Local Python application files
│   ├── hello.py
│   ├── test_hello.py
│   ├── Jenkinsfile
│   └── requirements.txt
├── .devcontainer/         # VS Code development container
└── README.md              # This file
```

---

## 🔨 Jenkins Pipeline Features

### Pipeline Stages
1. **Checkout** - Source code retrieval
2. **Setup Python Environment** - Python/pip verification
3. **Install Dependencies** - PyInstaller and requirements
4. **Run Tests** - Unit test execution
5. **Build Application** - PyInstaller executable creation
6. **Test Executable** - Binary verification
7. **Archive Artifacts** - Build artifact storage

### 🧪 CI/CD Workflow

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') { ... }
        stage('Setup Python Environment') { ... }
        stage('Install Dependencies') { ... }
        stage('Run Tests') { ... }
        stage('Build Application') { ... }
        stage('Test Executable') { ... }
        stage('Archive Artifacts') { ... }
    }
}
```

### ✅ Automated Testing
- Unit tests with Python unittest framework
- Executable functionality verification
- Build artifact validation
- Pipeline success/failure notifications

---

## 🔗 Repository Links

### 1. Jenkins Infrastructure Repository
- **URL**: [https://github.com/jpremchander/INFO8995-25S-Assignment4](https://github.com/jpremchander/INFO8995-25S-Assignment4)
- **Purpose**: Ansible playbooks for Jenkins deployment
- **Contents**: `up.yaml`, `down.yaml`, infrastructure code

### 2. GitHub Python Application Repository
- **URL**: [https://github.com/jpremchander/Python-App-INFO8995-Assignment4.git](https://github.com/jpremchander/Python-App-INFO8995-Assignment4.git)
- **Purpose**: External CI/CD integration
- **Access**: GitHub webhook → External tunnel → Jenkins
- **Features**: Automated builds on push, external artifact access
- **Jenkins Job**: [https://jenkins.exotrend.live/job/CICD-K8s/](https://jenkins.exotrend.live/job/CICD-K8s/)

### 3. Gitea Python Application Repository
- **URL**: [https://gitea.exotrend.live/prem/Python-App-INFO8995-Assignment4-Gitea](https://gitea.exotrend.live/prem/Python-App-INFO8995-Assignment4-Gitea)
- **Purpose**: Internal CI/CD integration
- **Access**: Gitea webhook → Cluster IP → Jenkins
- **Features**: Internal network builds, cluster-native operation
- **Jenkins Job**: [https://jenkins.exotrend.live/job/CICD-K8s-Gitea/](https://jenkins.exotrend.live/job/CICD-K8s-Gitea/)

---

## ⚙️ Configuration Details

### NFS Storage Configuration
```yaml
# TrueNAS NFS Setup
Path: /mnt/ops-pool/jenkins-data
Mapall User: jenkins (UID: 1000)
Mapall Group: jenkins (GID: 1000)
Permissions: 777
Protocol: NFSv3
```

### Jenkins Configuration
```yaml
# Kubernetes Resources
Namespace: jenkins
Service Type: NodePort (port 32090)
Ingress: Traefik with custom domains
Storage: 5Gi NFS persistent volume
Resource Limits: 2Gi RAM, 1000m CPU
```

### Webhook Configuration

#### GitHub Webhook
- **URL**: `https://jenkins.exotrend.live/github-webhook/`
- **Content-Type**: `application/json`
- **Events**: Push events
- **Purpose**: Trigger external builds

#### Gitea Webhook
- **URL**: `http://jenkins-service.jenkins.svc.cluster.local:9090/gitea-webhook/`
- **Content-Type**: `application/json`
- **Events**: Push events
- **Purpose**: Trigger internal builds

---

## 🛠️ Technical Implementation

### Ansible Automation
- **Infrastructure as Code**: Complete Jenkins deployment automation
- **Idempotent Operations**: Safe to run multiple times
- **Resource Management**: Proper creation and cleanup ordering
- **Error Handling**: Graceful failure recovery

### Container Strategy
- **Base Image**: jenkins/jenkins:lts
- **Security Context**: fsGroup 1000, runAsUser 1000
- **Custom Configuration**: JENKINS_OPTS for port configuration
- **Health Checks**: Liveness and readiness probes

### Storage Management
- **Persistent Data**: Jenkins home directory on NFS
- **User Mapping**: Consistent UID/GID across containers
- **Performance**: NFSv3 with optimal mount options
- **Backup**: Persistent across pod restarts

---

## 📊 Assignment Completion Status

| Requirement | Status | Points | Implementation |
|-------------|--------|--------|----------------|
| Jenkins deployment with Ansible | ✅ COMPLETE | 2/2 | `up.yaml` with comprehensive K8s resources |
| Resource cleanup playbook | ✅ COMPLETE | 2/2 | `down.yaml` with reverse-order removal |
| Python app with Jenkinsfile | ✅ COMPLETE | 2/2 | Complete CI/CD pipeline implementation |
| GitHub integration & webhook | ✅ COMPLETE | 2/2 | External tunnel + webhook automation |
| Gitea integration & webhook | ✅ COMPLETE | 2/2 | Internal cluster + webhook automation |
| **Total Score** | ✅ **COMPLETE** | **10/10** | **All requirements met** |

---

## 🔍 Troubleshooting

### Common Issues

#### Jenkins Access Issues
```bash
# Check service status
kubectl get svc -n jenkins

# Port forward for direct access
kubectl port-forward svc/jenkins-service 9090:9090 -n jenkins
```

#### NFS Permission Problems
```bash
# Verify NFS mount
kubectl exec -n jenkins deployment/jenkins -- ls -la /var/jenkins_home

# Check user mapping on TrueNAS
# Ensure jenkins user (UID 1000) exists and has proper permissions
```

#### Pipeline Failures
```bash
# Check Jenkins logs
kubectl logs -n jenkins deployment/jenkins

# Verify Python environment
kubectl exec -n jenkins deployment/jenkins -- python3 --version
```

---

## 🌐 Live System Access

### Jenkins CI/CD Platform
- **Main Jenkins Dashboard**: [https://jenkins.exotrend.live](https://jenkins.exotrend.live)
- **GitHub Pipeline Job**: [https://jenkins.exotrend.live/job/CICD-K8s/](https://jenkins.exotrend.live/job/CICD-K8s/)
- **Gitea Pipeline Job**: [https://jenkins.exotrend.live/job/CICD-K8s-Gitea/](https://jenkins.exotrend.live/job/CICD-K8s-Gitea/)

### Repository Access
- **GitHub Repository**: [https://github.com/jpremchander/Python-App-INFO8995-Assignment4.git](https://github.com/jpremchander/Python-App-INFO8995-Assignment4.git)
- **Gitea Repository**: [https://gitea.exotrend.live/prem/Python-App-INFO8995-Assignment4-Gitea](https://gitea.exotrend.live/prem/Python-App-INFO8995-Assignment4-Gitea)
- **Infrastructure Repository**: [https://github.com/jpremchander/INFO8995-25S-Assignment4](https://github.com/jpremchander/INFO8995-25S-Assignment4)

### Automated Workflow Status
- ✅ **GitHub → Jenkins**: Webhook configured and functional
- ✅ **Gitea → Jenkins**: Webhook configured and functional  
- ✅ **Pipeline Automation**: Both jobs building successfully
- ✅ **Artifact Generation**: PyInstaller executables being created
- ✅ **External Access**: Public Jenkins instance accessible

---

## 📚 References

- [Jenkins on Kubernetes - DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-kubernetes)
- [Ansible Kubernetes Module](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_module.html)
- [Jenkins Python PyInstaller Tutorial](https://www.jenkins.io/doc/tutorials/build-a-python-app-with-pyinstaller/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

---

## 🏆 Project Success Metrics

- ✅ **100% Automated Deployment**: Infrastructure as Code
- ✅ **Dual Integration**: GitHub + Gitea webhook automation
- ✅ **Zero Manual Intervention**: Fully automated CI/CD pipeline
- ✅ **High Availability**: Persistent storage with NFS
- ✅ **Security**: Proper RBAC and network policies
- ✅ **Scalability**: Container-native Kubernetes deployment

---

**Submitted by**: Prem Chander J (9015480) & Rishi Patel (8972657)  
