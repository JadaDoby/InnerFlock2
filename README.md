# InnerFlock2

## To run
```bash
cd runsever
```

``` bash
python manage.py runserver
```

[29/Feb/2024 20:36:07] "GET / HTTP/1.1" 200 3522
Token used too early, 1709238989 < 1709239708. Check that your computer's clock is set correctly.
[29/Feb/2024 20:36:29] "POST /verify-token/ HTTP/1.1" 200 55
If you get this error please run
```bash
sudo ntpdate time.google.com
```
