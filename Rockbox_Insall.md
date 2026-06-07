# Rockbox Installation Summary: 5th Gen iPod (Linux)

This guide summarizes the successful installation process for Rockbox on a 5th Generation iPod ("iPod Video") using a Linux environment.

## 1. Preparation
Ensure you have the necessary tools and firmware files downloaded to your working directory.
*   **ipodpatcher:** The tool used to patch the iPod's bootloader.
*   **rockbox-ipodvideo.zip:** The official Rockbox firmware package for your specific model.

## 2. Installing the Bootloader
1.  Ensure `ipodpatcher` is executable:
    `chmod +x ipodpatcher`
2.  Run the patcher in interactive mode:
    `sudo ./ipodpatcher`
3.  When prompted, enter **i** to install the bootloader.

## 3. Transferring Firmware Files
1.  **Identify the Mount Point:** Use `lsblk` to find the correct partition (e.g., `/media/alelawso/IPOD`).
2.  **Extract Files:** Unzip the firmware directly to the root of the iPod partition:
    `sudo unzip rockbox-ipodvideo.zip -d /media/alelawso/IPOD/`
3.  **Verify Structure:** Ensure the `.rockbox` folder is located at the root of the drive:
    `ls -la /media/alelawso/IPOD/`
4.  **Correct Placement (if necessary):** If files were extracted into a subfolder, move the `.rockbox` directory to the root:
    `sudo mv /media/alelawso/IPOD/rockbox-ipodvideo/.rockbox /media/alelawso/IPOD/`

## 4. Finalizing
1.  **Safely Unmount:** Always unmount the device before disconnecting:
    `sudo umount /media/alelawso/IPOD`
2.  **Hard Reset:** Disconnect the iPod and perform a hard reset by holding **Menu + Select** for 6-8 seconds.
3.  **Launch:** The device should now boot into the Rockbox interface.

## Troubleshooting
*   **"File not found":** This indicates the bootloader is running but cannot see the `.rockbox` folder. Verify that the folder exists at the root of the FAT32 partition.
*   **"Wrong fs type":** Ensure you are targeting the correct partition identified by `lsblk` and that the drive is formatted as FAT32.
