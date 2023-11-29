## Simple Task - Ansible (28-11-2023)

### 1. Buatlah inventory yang mendefinisikan variabel dan host
```yaml
all:
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
```
### 2. Buatlah playbook dengan task menjalankan docker container dan kriteria terdapat image, port, environment variables
```yaml
- name: Menjalankan docker container - Faiz
  hosts: btj-academy
  become: true
  tasks:
    - docker_container:
        name: faiz2
        image: "grad_app"
        interactive: true
        tty: true
        ports:
          - "8034:8034"
```

### Run ansible nya
1. Copy ssh from local to vm
```bash
scp C:\Users\USER\.ssh\id_rsa <user>@btj-academy.bangunindo.io:/home/<user>/.ssh/id_rsa
```
2. Create a local dockerfile for ansible in the same directory with `inventory.yaml` and `playbook.yaml`
```dockerfile
FROM python:3.9-alpine

RUN apk update && apk add build-base libffi-dev

RUN pip3 install ansible

COPY . .
```
3. Build the docker image for the local docker, and run the image as container
```bash
docker build -t lala
docker run -it -d -v C:/Users/faizk\.ssh\:/root/.ssh/ --name test lala
```
4. Enter the container, install openssh, and Change the permission of the ssh key
```bash
docker exec -it 2e0335ed6191 sh
apk add openssh
chmod -R 400 /root/.ssh/id_rsa*
```
5. Run ansible
```bash
ansible-playbook -i inventory.yaml playbook.yaml --user faizkhansaadrika
```
6. Login to ssh, and check/verify whether the container has been ran
```bash
ssh faizkhansaadrika@btj-academy.bangunindo.io
docker ps -a
```