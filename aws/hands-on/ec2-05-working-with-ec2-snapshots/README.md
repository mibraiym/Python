# Hands-on EC2-05 : Working with EC2 Snapshots

Purpose of the this hands-on training is to teach students how to take a snapshot of EC2 instance and create an image from EC2 instance.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- take snapshots of EC2 instances on AWS console.

- create images from EC2 instances on AWS console.

- understand of difference between the image and the snapshot.

- create different types of AMI.

## Outline

- Part 1 - Creating an Image from the Snapshot of the Nginx Server and Launching a new Instance

- Part 2 - Creating an Image and Launching an Instance from the same Image

- Part 3 - Creating an Image from the Snapshot of the Root Volume and Launching a new Instance

- Part 4 - Creating an Image from Customized Instance and Launching an instance from the same AMI

![Apache HTTP Server](./ami_lifecycle.png)

## Part 1 - Creating an Image from the Snapshot of the Nginx Server and Launching a new Instance

- Launch an instance with following configurations.

  - Security Group: Allow SSH and HTTP ports from anywhere

  - User data (paste it for Nginx)

  ```bash
  #!/bin/bash
  yum update -y
  amazon-linux-extras install nginx1.12
  yum install wget -y
  chkconfig nginx on
  cd /usr/share/nginx/html
  chmod o+w /usr/share/nginx/html
  rm index.html
  wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
  wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
  service nginx start
  ```

  - Key: Name --> Value: SampleInstance  

- Go to EC2 dashboard and click snapshot section from left-hand menu.

- Click `create snapshot` button.

```text
Select resource type : Instance
Instance ID          : Select the instance ID of Nginx
```

- Click create snapshot.

- Click snapshot `Action` menu and select `create image`

```text
Name        : ClaruswayAMI_1
Description : ClaruswayAMI_1
```

- Click the `launch instance` tab.

- Click `myAMI` from left-hand menu.

- Select `ClaruswayAMI_1`

- Show that security group rules (SSH, HTTP) and `user data` same as original EC2 Nginx instance.

- Launch instance.

- Copy the public IP of the newly created instance and paste it to the browser.

- Show that the Nginx Web Server is working.

## Part 2 - Creating an Image and Launching an Instance from the same Image

- Go to `SampleInstance`

- Click the actions menu.

- Select image >> create image.

```text
Name        : ClaruswayAMI_2
Description : ClaruswayAMI_2
```

- Click AMI section from left hand menu and show `ClaruswayAMI_2`

- After ClaruswayAMI creation process is completed, click snapshot section from left-hand menu.

- Show that AWS has created a new snapshot for newly created `ClaruswayAMI_2` image.

- Click the `launch instance` tab.

- Click `myAMI` from left-hand menu.

- Select `ClaruswayAMI_2`.

- Show that security group rules (SSH, HTTP) and `user data` same as original EC2 Nginx instance.

- Launch instance.

- Copy the public IP of the newly created instance and paste it to the browser.

- Show that the Nginx Web Server is working.

## Part 3 - Creating an Image from the Snapshot of the Root Volume and Launching a new Instance

- Go to EC2 menu and click snapshot section from left-hand menu.

- Click `create snapshot` button.

```text
Select resource type : Volume
Instance ID : select the root volume of the SampleInstance
```

- Click create snapshot.

```text
Name        : ClaruswayAMI_3
Description : ClaruswayAMI_3
```

- Click the `launch instance` tab.

- Click `myAMI` from left-hand menu.

- Select `ClaruswayAMI_3`.

- Show that security group rules (SSH, HTTP) and `user data` same as original EC2 Nginx instance.

- Launch instance.

- Copy the public IP of the newly created instance and paste it to the browser.

- Show that the Nginx Web Server is working.

## Part 4 - Creating an Image from Customized Instance and Launching an instance from the same AMI

- Connect to `SampleInstance` with SSH.

- Create a file named `i_am_here.txt`

```bash
touch i_am_here.txt
ls
```

- Exit from the instance.

- Go to EC2 console.

- Select the instance named `SampleInstance`.

- Click the actions menu.

- Select image >> create image.

```text
Name        : ClaruswayAMI_4
Description : ClaruswayAMI_4
```

- Click the `launch instance` tab.

- Click `myAMI` from left-hand menu

- Select `ClaruswayAMI_4`

- Launch instance.

```text
Name        : ClaruswayAMI_5
Description : ClaruswayAMI_5
```

- Connect to `ClaruswayAMI_5` with SSH.

- Show `i_am_here.txt` with `ls`.

```bash
ls
```
