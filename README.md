# rascal17

install:

`sudo apt-get install xboxdrv`

debug controller:

```
git clone https://github.com/martinohanlon/XboxController
cp XboxController/XboxContoller.py pathToYourProject
sudo xboxdrv --silent --detach-kernel-driver &
python XboxController.py
```

[more about XboxController library](http://www.stuffaboutcode.com/2014/10/raspberry-pi-xbox-360-controller-python.html)
