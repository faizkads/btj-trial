# btj-trial

Hi! this is the first version of the repo! **graduates.py** is a simple script to determine the student's graduation based on the score and absence

## Simple Task - Ansible

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
5. Enter the container, install openssh, and Change the permission of the ssh key
```bash
docker exec -it 2e0335ed6191 sh
apk add openssh
chmod -R 400 /root/.ssh/id_rsa*
```
3. Run ansible
```bash
ansible-playbook -i inventory.yaml playbook.yaml --user faizkhansaadrika
```

## Simple Task - Docker Image

### 1. Buatlah image dari aplikasi sederhana yang sudah dibuat
Steps:
1. Create dockerfile on local and push to github
2. Login SSH `ssh faizkhansaadrika@btj-academy.bangunindo.io`
3. Clone repo using `git clone https://github.com/faizkads/btj-trial.git`
4. Build the docker image using `docker build -t grad-app .`
5. Verify with `docker images`

### 2. Jalankan image tersebut sebagai container dan berjalan pada port 8081
```bash
docker run -it -d --expose 8081 --name faiz grad_app`
```
atau saya juga baca bisa dengan
```bash
docker run -it -d -p 8081:8081 --name faiz grad_app`
```
### 3. Berapakah IP docker container whoami?
```bash
docker inspect whoami
output:
...
	"IPAddress": "172.17.0.2",
```
### 4. Apa isi dari file yang tersembunyi dari docker container whoami?
1. check colume mount dari whoami dengan `docker inspect whoami`
2. `docker exec -it f301b98cba61 /bin/sh`
3. `ls tmp/system`
4. `cat tmp/system/whoami`
output:
`Oofooni1eeb9aengol3feekiph6fieve`

### 5. Image apa yang digunakan pada docker container whoami?
1. `docker ps`
2.  Image name dari whoami adalah `secret:aequaix9De6dii1ay4HeeWai2obie6Ei`
