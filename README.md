# Opencv Chinese Flag

Add the Chinese flag to your avatar. (Happy National Day!)

## Demo

![site](img/site.png)
| Original Avatar| Add Chinese Flag |
|:--------------:|:----------------:|
|![demo](img/demo.png)|![_new](img/_new.jpg)|

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
git clone https://github.com/XavierJiezou/opencv-chinese-flag.git
cd opencv-chinese-flag
python app.py
```

## Deploy

1. Download and install Docker.
> [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Pull the container
```bash
docker pull xavierjiezou/opencv-chinese-flag:latest
```
3. Run the container in detached mode.
```bash
docker run --rm -d -p 5001:5000 --name opencv-chinese-flag xavierjiezou/opencv-chinese-flag
```
---
Finally, you can visit `YOUR_PUBLIC_IP_ADDRESS:5001` in your browser to have a look.

## Nginx

### Nginx

1. Download and install Nginx.
> [http://nginx.org/en/docs/install.html](http://nginx.org/en/docs/install.html)
2. Get path of the configuration file.
```bash 
$ nginx -t
nginx: the configuration file /www/server/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /www/server/nginx/conf/nginx.conf test is successful
```
3. Add the following contents to the configuration file.
```bash
server {
    listen       5003;
    server_name  localhost;

    location / {
        proxy_pass http://localhost:5001/;
    }
}
```
---
Then, you can visit `YOUR_PUBLIC_IP_ADDRESS:5003` in your browser to have a look.

### Docker-Nginx

1. Download and install Docker.
> [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Pull the container
```bash
docker pull nginx
```
3. Run the container in detached mode.
```bash
docker run --rm  -d -p 5002:80 --name nginx-opencv-chinese-flag \
-v /root/nginx/log:/var/log/nginx \
-v /root/nginx/default.conf:/etc/nginx/conf.d/default.conf \
nginx
```
---
- Map your directory `/root/nginx/log` in local machine to the directory `/var/log/nginx` in docker container.
- Map your file `/root/nginx/default.conf` in local machine to the file `/etc/nginx/conf.d/default.conf` in docker container.
---
Add the following contents to the configuration file `/root/nginx/default.conf`. 
```bash
server {
    listen       80;
    server_name  localhost;

    location / {
        proxy_pass http://172.17.0.3:5000;
    }
}
```
`172.17.0.3` is the docker container's `IPAddress`, you can get it by running the command:
```bash
docker inspect --format '{{ .NetworkSettings.IPAddress }}' opencv-chinese-flag
```

## Algorithm

```
python algorithm.py img/demo.png
```

## Flag

| 1024x683| 2048x1366 | 4096x2731 |
|:-------:|:---------:|:---------:|
|![1024](img/guoqi/guoqi_1024.png)|![2048](img/guoqi/guoqi_2048.png)|![4096](img/guoqi/guoqi_4096.png)|

## Reference

> - Flag: [http://www.gov.cn/guoqing/20201231/guoqi.zip](http://www.gov.cn/guoqing/20201231/guoqi.zip)
> - Demo: [https://v.douyin.com/dx6JUoo/](https://v.douyin.com/dx6JUoo/)
> - Code: [https://docs.opencv.org/master/d6/d00/tutorial_py_root.html](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
> - The gradient of flag is made by [Adobe Photoshop](https://www.adobe.com/products/photoshop.html).
