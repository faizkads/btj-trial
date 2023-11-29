# btj-trial - Faiz Khansa Adrika

Hi! this is the first version of the repo!

## Simple Task - Ansible (28-11-2023)
check in folder `ansible`

## Simple Task - Flask Deployment (28-11-2023)
check in folder `flask-task`

## Simple Task - Docker Image (27-11-2023)

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
1. check volume mount dari whoami dengan `docker inspect whoami`
2. `docker exec -it f301b98cba61 /bin/sh`
3. `ls tmp/system`
4. `cat tmp/system/whoami`
output:
`Oofooni1eeb9aengol3feekiph6fieve`

### 5. Image apa yang digunakan pada docker container whoami?
1. `docker ps`
2.  Image name dari whoami adalah `secret:aequaix9De6dii1ay4HeeWai2obie6Ei`
