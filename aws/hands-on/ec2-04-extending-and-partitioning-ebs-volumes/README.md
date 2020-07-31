# Hands-on EC2-04 : Extending and Partitioning EBS Volumes

Purpose of the this hands-on training is to teach the students how to add or attach an EBS (Elastic Block Storage) volume on an AWS instance, how to extend and resize volumes, and how to create partitions in volumes on running Amazon Linux 2 EC2 instances.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- understand what is the difference between root volume and EBS Volume.

- list volumes to show current status of primary (root) and additional volumes

- demonstrate their knowledge on how to create EBS volume.

- create mounting point on EC2 instances.

- partition volume on EC2 instances.

- resize the volume or partitions on the new EBS volumes.

- understand how to auto-mount EBS volumes and partitions after reboots.

## Outline

- Part 1 - Extend EBS Volume without Partitioning

- Part 2 - Extend EBS Volume with Partitioning

- Part 3 - Auto-mount EBS Volumes and Partitions on Reboot

![EBS Volumes](./ebs_backed_instance.png)

## Part 1 - Extend EBS Volume without Partitioning

- Launch an instance from AWS console, check which volumes attached to instance. Only root volume should be listed

```bash
lsblk
```

- Create a new volume from AWS console, attach the new volume from AWS console, then list block storages again. Root volume and secondary volume should be listed.

```text
PS: Volume AZ and EC2 AZ have to be same.

Volume Type : General Purpose SSD
Size (GiB): 8 GB
The Rest can keep it as it is

Attach this volume to EC2 with Action ---> Attach Volume
If EC2 and volume are not in the same AZ, we can not see the EC2 that we would attach the volume on the list.
```

```bash
lsblk
```

- Check if the attached volume is already formatted or not and has data on it.

```bash
sudo file -s /dev/xvdf
```

- If not formatted, format the new volume.

```bash
sudo mkfs -t ext4 /dev/xvdf
```

- Create a mounting point path for new volume.

```bash
sudo mkdir /mnt/2nd-vol
```

- Mount the new volume to the mounting point path.

```bash
sudo mount /dev/xvdf /mnt/2nd-vol/
```

- Check if the attached volume is mounted to the mounting point path.

```bash
lsblk
```

- Show the available space, on the mounting point path.

```bash
df -h
```

- If there is data on it, check if the data still persists.

```bash
ls -lh /mnt/2nd-vol/
```

- If there is no data on it, create a new file to show persistence in later steps.

```bash
cd /mnt/2nd-vol
sudo touch who-wants-to-live-forever.txt
ls
```

- Modify the new volume in AWS console, and enlarge capacity to double gb. (Volume ----> Select the volume that will be resized ----> Action ---> Modify Volume ----> Add size the current amount)

- Check if the attached volume is showing the new capacity.

```bash
lsblk
```

- Show the real capacity used currently at mounting path, old capacity should be shown.

```bash
df -h
```

- Resize the file system on the new volume to cover all available space.

```bash
sudo resize2fs /dev/xvdf
```

- Show the real capacity used currently at mounting path, new capacity should reflect modified volume size.

```bash
df -h
```

- Show that the data still persists on the newly enlarged volume.

```bash
ls -lh /mnt/2nd-vol/
```

- Show that mounting point path will be gone when instance rebooted.

```bash
sudo reboot now
```

- Show the new volume is still attached, but not mounted

```bash
lsblk
```

- Check if the attached volume is already formatted or not and has data on it.

```bash
sudo file -s /dev/xvdf
```

- Mount the new volume to the mounting point path

```bash
sudo mount /dev/xvdf /mnt/2nd-vol/
```

- Show the used and available capacity is same as the disk size.

```bash
df -h
```

- If there is data on it, check if the data still persists.

```bash
ls -lh /mnt/2nd-vol/
```

- We can see the file named who-wants-to-live-forever.txt

## Part 2 - Extend EBS Volume with Partitioning

- List volumes to show current status, primary (root) and secondary volumes should be listed.

```bash
lsblk
```

- Show the used and available capacities related with volumes.

```bash
df -h
```

- Create tertiary volume on AWS console

- Attach the new volume from AWS console, then list volumes again. Primary (root), secondary and tertiary volumes should be listed

```text
Volume Type : General Purpose SSD (pg2)
Size (GIB) : Double GB
Availability Zone : Same as EC2
The rest can keep them as it is

Select tertiary Volume ----> Action -----> Attach  Volume ----> Attach it EC2
```

```bash
lsblk
```

- Show the used and available capacities related with volumes.

```bash
df -h
```

- Show the current partitions. Use `fdisk -l /dev/xvda` for specific partition.

```bash
sudo fdisk -l
```

- Check all available `fdisk` commands.

```bash
sudo fdisk /dev/xvdg

- n -> add new partition (with 2G size)
- p -> primary
- Partition number: 1
- Last sector: +1500M
- n -> add new partition (with rest of the size)
- p -> primary
- Partition number: 2
- p -> show the partition table
- w -> write partition table
- show new partitions
```

```bash
lsblk
```

- Format the new partitions.

```bash
sudo mkfs -t ext4 /dev/xvdg1
sudo mkfs -t ext4 /dev/xvdg2
```

- Create a mounting point path for new partitions.

```bash
sudo mkdir /mnt/3rd-vol-part1
sudo mkdir /mnt/3rd-vol-part2
```

- Mount the new partitions to the mounting point path

```bash
sudo mount /dev/xvdg1 /mnt/3rd-vol-part1/
sudo mount /dev/xvdg2 /mnt/3rd-vol-part2/
```

- List volumes to show current status, all volumes and partitions should be listed

```bash
lsblk
```

- Show the used and available capacities related with volumes and partitions.

```bash
df -h
```

- If there is no data on it, create a new file to show persistence in later steps.

```bash
sudo touch /mnt/3rd-vol-part2/i-want-to-survive.txt
ls -lh /mnt/3rd-vol-part2/
```

- Modify the new volume in AWS console, and enlarge capacity to double gb.

- Check if the attached volume is showing the new capacity or not.

```bash
lsblk
```

- Show the real capacity used currently at mounting path, old capacity should be shown.

```bash
df -h
```

- Extend the partition 2 and occupy all newly available space.

```bash
sudo growpart /dev/xvdg 2
```

- Show the real capacity used currently at mounting path, updated capacity should be shown.

```bash
df -h
```

- Resize and extend the file system.

```bash
sudo resize2fs /dev/xvdg2
```

- Show and save the UUIDs of each volume and partitions.

```bash
sudo file -s /dev/xvdf
sudo file -s /dev/xvdg
sudo file -s /dev/xvdg1
sudo file -s /dev/xvdg2
```

- Reboot and show that configuration is gone.

```bash
sudo reboot now
```

## Part 3 - Auto-mount EBS Volumes and Partitions on Reboot

- secondary volume UUID=7184edc1-1ff9-4bb7-bc63-569c8c2110f1 (Please enter your volume ID)

- tertiary volume partition 1 UUID=e650e57c-e031-4f6e-a46a-313ee50acd5a (Please enter your volume ID)

- tertiary volume partition 2 UUID=560292eb-2316-4a8b-83ad-517aedc87a30 (Please enter your volume ID)

- Back up the `/etc/fstab` file.

```bash
sudo cp /etc/fstab /etc/fstab.bak
```

- Open `/etc/fstab` file and make an entry in the following format.

```text
/dev/xvdf       /newvolume   ext4    defaults,nofail        0       0
```

```bash
sudo vim /etc/fstab
```

- Mount volumes and partitions with `fstab` file.

```bash
sudo mount -a
```

- List volumes to show current status, all volumes and partitions should be listed.

```bash
lsblk
```

- Show the used and available capacities related with volumes and partitions.

```bash
df -h
```

- If there is data on it, check if the data still persists.

```bash
ls -lh /mnt/2nd-vol/
ls -lh /mnt/3rd-vol-part2/
```

- Reboot and show that configuration is gone.

```bash
sudo reboot now
```

- List volumes to show current status, all volumes and partitions should be listed.

```bash
lsblk
```

- Show the used and available capacities related with volumes and partitions.

```bash
df -h
```

- If there is data on it, check if the data still persists.

```bash
ls -lh /mnt/2nd-vol/
ls -lh /mnt/3rd-vol-part2/
```

## Resources

- [Extending a Linux file system after resizing a volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html)

- [10 fdisk Commands to Manage Linux Disk Partitions](https://www.tecmint.com/fdisk-commands-to-manage-linux-disk-partitions/)
