# Mikrotik Multithreading Automation with Python 
Multithreading enables CPUs to run different parts(threads) of a process concurrently.
1. You must first enable ssh on your mikrotik router and access them over the network
2. Install prerequisites
```python
pip install netmiko

pip install paramiko
```
3.  Put name , IP address and password of mikrotik devices in order and line by line in the `devices_list.txt` file
4.  Put all the commands of your mikrotik router device in order and line by line in the `commands_all_devices` file
5.  Run `mikrotik-automation.py`
```python
py mikrotik-automation.py
```

**NOTE**: Username in all device is the same `Username = admin`

> Python Version : 3.10

<p align=center><b>:fire: Learn as if you will live forever, live like you will die tomorrow :fire:</p>
