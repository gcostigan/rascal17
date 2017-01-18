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

