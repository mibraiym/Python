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

- Create a new volume from AWS console, attach the new volume from AWS console, then list block storages again. Root volume and secondary volume should be listed.

```text
PS: Volume AZ and EC2 AZ have to be same.

Volume Type : General Purpose SSD
Size (GiB): 8 GB
The Rest can keep it as it is

Attach this volume to EC2 with Action ---> Attach Volume
If EC2 and volume are not in the same AZ, we can not see the EC2 that we would attach the volume on the list.
```

- Check if the attached volume is already formatted or not and has data on it.

- If not formatted, format the new volume.

- Create a mounting point path for new volume.

- Mount the new volume to the mounting point path.

- Check if the attached volume is mounted to the mounting point path.

- Show the available space, on the mounting point path.

- If there is data on it, check if the data still persists.

- If there is no data on it, create a new file to show persistence in later steps.

- Modify the new volume in AWS console, and enlarge capacity to double gb. (Volume ----> Select the volume that will be resized ----> Action ---> Modify Volume ----> Add size the current amount)

- Check if the attached volume is showing the new capacity.

- Show the real capacity used currently at mounting path, old capacity should be shown.

- Resize the file system on the new volume to cover all available space.

- Show the real capacity used currently at mounting path, new capacity should reflect modified volume size.

- Show that the data still persists on the newly enlarged volume.

- Show that mounting point path will be gone when instance rebooted.

- Show the new volume is still attached, but not mounted

- Check if the attached volume is already formatted or not and has data on it.

- Mount the new volume to the mounting point path

- Show the used and available capacity is same as the disk size.

- If there is data on it, check if the data still persists.

- We can see the file named `who-wants-to-live-forever.txt`

## Part 2 - Extend EBS Volume with Partitioning

- List volumes to show current status, primary (root) and secondary volumes should be listed.

- Show the used and available capacities related with volumes.

- Create tertiary volume on AWS console

- Attach the new volume from AWS console, then list volumes again. Primary (root), secondary and tertiary volumes should be listed

```text
Volume Type : General Purpose SSD (pg2)
Size (GIB) : Double GB
Availability Zone : Same as EC2
The rest can keep them as it is

Select tertiary Volume ----> Action -----> Attach  Volume ----> Attach it EC2
```

- Show the used and available capacities related with volumes.

- Show the current partitions. Use `fdisk -l /dev/xvda` for specific partition.

- Check all available `fdisk` commands.

- Format the new partitions.

- Create a mounting point path for new partitions.

- Mount the new partitions to the mounting point path

- List volumes to show current status, all volumes and partitions should be listed

- Show the used and available capacities related with volumes and partitions.

- If there is no data on it, create a new file to show persistence in later steps.

- Modify the new volume in AWS console, and enlarge capacity to double gb.

- Check if the attached volume is showing the new capacity or not.

- Show the real capacity used currently at mounting path, old capacity should be shown.

- Extend the partition 2 and occupy all newly available space.

- Show the real capacity used currently at mounting path, updated capacity should be shown.

- Resize and extend the file system.

- Show and save the UUIDs of each volume and partitions.

- Reboot and show that configuration is gone.

## Part 3 - Auto-mount EBS Volumes and Partitions on Reboot

- secondary volume UUID=7184edc1-1ff9-4bb7-bc63-569c8c2110f1 (Please enter your volume ID)

- tertiary volume partition 1 UUID=e650e57c-e031-4f6e-a46a-313ee50acd5a (Please enter your volume ID)

- tertiary volume partition 2 UUID=560292eb-2316-4a8b-83ad-517aedc87a30 (Please enter your volume ID)

- Back up the `/etc/fstab` file.

- Open `/etc/fstab` file and make an entry in the following format.

```text
/dev/xvdf       /newvolume   ext4    defaults,nofail        0       0
```

- Mount volumes and partitions with `fstab` file.

- List volumes to show current status, all volumes and partitions should be listed.

- Show the used and available capacities related with volumes and partitions.

- If there is data on it, check if the data still persists.

- Reboot and show that configuration is gone.

- List volumes to show current status, all volumes and partitions should be listed.

- Show the used and available capacities related with volumes and partitions.

- If there is data on it, check if the data still persists.

## Resources

- [Extending a Linux file system after resizing a volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html)

- [10 fdisk Commands to Manage Linux Disk Partitions](https://www.tecmint.com/fdisk-commands-to-manage-linux-disk-partitions/)
