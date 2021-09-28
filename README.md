# Silicon Compute
![silicon logo](https://i.imgur.com/XhUrBqz.png)

# Video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Gi41kjjyGbU/0.jpg)](https://www.youtube.com/watch?v=Gi41kjjyGbU)

Open source cloud compute solution designed to simplify and streamline the process of offloading rendering tasks on AWS and Google Cloud Compute with Blender.

Even though silicon was designed from the ground up to work with blender it can work with anything that provides command line rendering operators.

The main server is written in Python for easy integration.

The process is as follows:

SSH into remote server > Clone and deploy silicon > Make sure the server is running by visiting http://<remote_server_ip:5000

Once you're sure the server is running you can then upload a .blend file > go to render image or animation and type in the parameters you need.
