## Simple Task - Flask Deployment (28-11-2023)

### 1. Buat python app dan tambahkan beberapa routing kemudian custom port yang di-listen (Default 5000)
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/contact')
def view_contact():
    return 'This is the contact page'

@app.route('/products')
def view_products():
    return 'Its our first deployment, we dont have any products yet'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5003)
```

Dockerfile untuk remote server
```dockerfile
FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python","app.py" ]
```
### 2. Buatlah 1 playbook dengan beberapa task yaitu:
1. Menyalin file dari local ke server bj-academy
2. Build docker image untuk python app
3. Jalankan container yang sudah di build

playbook.yaml:
```yaml
- name: Simple Task 2 to Deploy Flask App - Faiz
  hosts: btj-academy
  become: true
  tasks:
    - name: Copy files inside flask folder to remote server
      copy:
        src: "./flask/"
        dest: "{{ vmPath }}"

    - name: Build docker image
      community.docker.docker_image:
        name: "{{ imageName }}"
        tag: "{{ imgTag }}"
        build:
          path: "{{ vmPath }}"
        source: build

    - name: Run docker container
      docker_container:
          name: "{{ contName }}"
          image: "{{ imageName }}:{{ imgTag }}"
          interactive: true
          tty: true
          ports:
            - "{{port}}"
```
inventory.yaml
```yaml
aall:
  vars:
    contName: flask-faiz2
    imageName: flaskapp-faiz
    imgTag: 0.0.1
    vmPath: /home/faizkhansaadrika/task2
    port: 5003:5003
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
```


### Execution
1. Create a local dockerfile to run ansible in docker, in the same directory with `inventory.yaml` and `playbook.yaml`
```dockerfile
FROM python:3.9-alpine

RUN apk update && apk add build-base libffi-dev

RUN pip3 install ansible

COPY . .
```
3. Build the docker image for the local docker, and run the image as container
```bash
docker build -t ansible
docker run -it -d -v C:/Users/faizk\.ssh\:/root/.ssh/ --name faiz ansible
```
4. Enter the container, install openssh, and Change the permission of the ssh key
```bash
docker exec -it 50a8693fb19d sh
apk add openssh
chmod -R 400 /root/.ssh/id_rsa*
```
5. Run ansible
```bash
ansible-playbook -i inventory.yaml playbook.yaml --user faizkhansaadrika
```
6. Login to ssh, and check/verify whether the files has been copied and the container has been ran
```bash
ssh faizkhansaadrika@btj-academy.bangunindo.io
ls ../task2
docker ps -a | grep flask-faiz
```

Check the routes:

http://btj-academy.bangunindo.io:5003/

http://btj-academy.bangunindo.io:5003/contact

http://btj-academy.bangunindo.io:5003/products
