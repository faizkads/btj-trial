# btj-trial

Hi! this is the first version of the repo! **graduates.py** is a simple script to determine the student's graduation based on the score and absence

## Simple Task - Ansible

### 1. Buatlah inventory yang mendefinisikan variabel dan host
```
all:
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
```
### 2. Buatlah playbook dengan task menjalankan docker container dan kriteria terdapat image, port, environment variables
```
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
          - '8019'
```

### Run ansible nya
1. Copy ssh from local to vm
```
scp C:\Users\USER\.ssh\id_rsa <user>@btj-academy.bangunindo.io:/home/<user>/.ssh/id_rsa![image](https://github.com/faizkads/btj-trial/assets/56906493/70745ff3-9360-4e30-9288-6041ee621bdd)
```
2. Change permission key yang di-copy
```
chmod -R 400 /home/<user>/.ssh/id_rsa*
```
3. Run ansible
```
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
`docker run -it -d --expose 8081 --name faiz grad_app`
atau saya juga baca bisa dengan
`docker run -it -d -p 8081:8081 --name faiz grad_app`
### 3. Berapakah IP docker container whoami?
```
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
