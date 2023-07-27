# Mikrotik Multiprocessing Automation with Python 
Multiprocessing enables CPUs to run different parts(process) of a process concurrently.
1. You must first enable ssh on your mikrotik router and access them over the network
2. Install prerequisites
```python
pip install netmiko

pip install paramiko

pip install colorama
```
3.  Put device name , IP address and password of mikrotik devices in order and line by line in the `devices_list.txt` file
4.  Put all the commands of your mikrotik router device in order and line by line in the `commands_all_devices` file
5.  Run `mikrotik-automation.py`
```python
py mikrotik-automation.py
```
6. For see result open `log.csv`

**NOTE**: Username in all device is the same `Username = admin`

> Python Version : 3.10

<p align=center><b>:fire: Learn as if you will live forever, live like you will die tomorrow :fire:</p>
