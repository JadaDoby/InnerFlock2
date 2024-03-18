# InnerFlock2

## To run
```bash
cd myproject
```

``` bash
python manage.py runserver
```
### Python module downloads
```bash
pip install python-decouple
```

[29/Feb/2024 20:36:07] "GET / HTTP/1.1" 200 3522
Token used too early, 1709238989 < 1709239708. Check that your computer's clock is set correctly.
[29/Feb/2024 20:36:29] "POST /verify-token/ HTTP/1.1" 200 55

### If you see this please run for linux/macos

```bash
sudo ntpdate time.google.com
```

## For windows
The Windows equivalent to the Linux command `sudo ntpdate time.google.com` (which sets the system's date and time by synchronizing with the time server specified, in this case, `time.google.com`) involves using the Windows Time Service (`w32time`). However, Windows does not use a direct equivalent command for immediate synchronization in the same way `ntpdate` does on Linux.

To achieve a similar effect on Windows, you can force a manual synchronization with an NTP server using the Command Prompt or PowerShell. Here's how you can do it:

### Using Command Prompt

1. Open Command Prompt as Administrator.
2. To configure the NTP server, use the following command:
   ```
   net stop w32time
   w32tm /config /manualpeerlist:time.google.com /syncfromflags:manual /reliable:YES /update
   net start w32time
   ```
3. To force the synchronization, use:
   ```
   w32tm /resync
   ```

### Using PowerShell

1. Open PowerShell as Administrator.
2. To configure the NTP server and force a synchronization, you can use the same commands as in the Command Prompt example above, since PowerShell can also execute Command Prompt commands.

This process manually configures `time.google.com` as the NTP server and then forces Windows to synchronize the system clock with it. 

Remember, these steps manually configure and synchronize time once. Windows automatically handles time synchronization at regular intervals through the Windows Time Service, so manual intervention is typically not required unless troubleshooting or precise time synchronization is needed immediately.
