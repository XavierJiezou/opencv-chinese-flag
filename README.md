# Introduction
Add the Chinese flag to your avatar. (Happy National Day!)
# Demo
| Original Avatar| Add Chinese Flag |
|:--------------:|:----------------:|
|![demo](img/demo.png)|![_new](img/_new.jpg)|
# Install
```bash
pip install -r requirements.txt
```
# Usage
```bash
git clone https://github.com/XavierJiezou/opencv-chinese-flag.git
cd opencv-chinese-flag
python app.py
```
# Deploy
1. Download and install Docker.
> [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Pull the container
```bash
docker pull xavierjiezou/opencv-chinese-flag:latest
```
3. Run the container in detached mode.
```bash
docker run -d -p 5001:5000 --name opencv-chinese-flag xavierjiezou/opencv-chinese-flag
```
---
Finally, you can visit `YOUR_IP_ADDRESS:5001` in your browser to have a look.
# Algorithm
```
python algorithm.py img/demo.png
```
# Flag
| 1024x683| 2048x1366 | 4096x2731 |
|:-------:|:---------:|:---------:|
|![1024](img/guoqi/guoqi_1024.png)|![2048](img/guoqi/guoqi_2048.png)|![4096](img/guoqi/guoqi_4096.png)|
# Reference
> Flag: [http://www.gov.cn/guoqing/20201231/guoqi.zip](http://www.gov.cn/guoqing/20201231/guoqi.zip)
> 
> Demo: [https://v.douyin.com/dx6JUoo/](https://v.douyin.com/dx6JUoo/)
> 
> Code: [https://docs.opencv.org/master/d6/d00/tutorial_py_root.html](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
> 
> The gradient of flag is made by [Adobe Photoshop](https://www.adobe.com/products/photoshop.html).