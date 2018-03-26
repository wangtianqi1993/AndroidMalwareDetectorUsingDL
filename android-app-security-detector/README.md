# Android App's malwares and adwares detector

## Description

This is an detector used [Androguard](https://github.com/androguard/androguard) and Machine Learning methods 
detector Adwares and malwares.

## Development

安装detector的开发环境，建议在python的virtualenv下开发，由于detector涉及到的依赖包较多建议先手动安装一些依赖包
- python2.7、numpy、scipy、scikit-learn

1. Git clone

```sh
    $ git clone http://gitlab.buptnsrc.com/android-security/android-app-security-detector.git
```

2. Python VirtualEnv

```sh
    $ sudo apt-get install python-virtualenv libffi-dev
    $ virtualenv -p python2.7 ~/VirtualEnv/detector --distribute
    $ source ~/VirtualEnv/detector/bin/activate
    $ cd android-app-security-detector
    $ python setup.py install(develop)
```

在安装过程中很可能会出现一些包依赖问题，主要问题是在numpy、scipy和scikit-learn
具体问题解决方法可以参考以下部分：
- scipy: http://www.scipy.org/install.html
- numpy: http://www.numpy.org/
- scikit-learn: http://scikit-learn.org/stable/install.html
- pip install scipy: http://stackoverflow.com/questions/26575587/cant-install-scipy-through-pip

在开发过程可以在pycharm中设置使用刚才建好的virtualenv, enjoy it~ :smile:

## Debug

 - 1.在PyCharm设置一个python解释器,最好是本地建立好的虚拟环境
 - 2.运行debug.py文件使用debug模式(右击选择'Debug')
 - 3.在你需要查看问题的代码之前设置断点,debug it~ :satisfied:

## Deploy

为了方便在服务器上部署detector程序，我们使用supervisor+gunicorn+virtualenv环境下部署程序：

 - 1.准备环境，具体操作如下：
 
```sh
    $ sudo apt-get install python-pip  
    $ sudo apt-get install python-dev       
    $ sudo pip install virtualenv       
    $ sudo apt-get install supervisor    
```

 - 2.将代码clone到服务器上,在服务器上创建一个python虚拟环境,具体操作可以参考[Development](#Development)部分
 
 - 3.将detector-gunicorn.conf拷贝至服务器/etc/supervisor/conf.d/ 目录下,同时需要保证/etc/supervisor/supervisord.conf
     中的include已经包括/etc/supervisor/conf.d目录. 并修改相应的参数内容。 具体操作如下：
     
```sh
    $ sudo cp detector-gunicorn.conf /etc/supervisor/conf.d/
    $ sudo supervisorctl reload  
    $ sudo supervisorctl start detector-gunicorn 
```

### Use and API
 TODO soon.
