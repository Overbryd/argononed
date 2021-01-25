The case is awesome.

The software is horrible. If you ever downloaded that messy "installation script" that is
the Python script of Argon ONE to control its fan...

You cannot unsee that stuff. If you still want to, here is the original:

https://download.argon40.com/argon1.sh

I have taken the liberty to extract the necessary Python script and systemd unit,
so you can put it on your RPi and be happy, not having to download and execute that Bash-mess
on your Pi.

## Setup

* Install dependencies

    ```
    sudo apt install -y python3-rpi.gpio python3-smbus
    ```

* Copy the scripts and profit
