AnimeTube
=========
AnimeTube is an api that parses websites for anime video content. Originally
the project aimed to be a full blown application for viewing anime directly
from command line but the views have since changed. As of now AnimeTube 
assists you by taking a name as input (doesn't matter how) parsing it through
all its available plugins (more on this later), or a specific one and returning
a link to the actual content. Thats it, that's all it does, after which the user
can choose how to handle the return content (most of the time you'll want to run
it through your local media player).



## ALPHA STAGE !!! 

##### How To Install:
AnimeTube uses setuptools to install any missing dependencies for the api to work 
correctly. If your current system does not have setuptools installed you can install
it by running the provided **ez_setup.py** file with `python ez_setup.py`. This will
install setuptools for you. After which you can run **setup.py** to install any missing
dependencies by `python setup.py install`. At this point you should have any
required dependency for AnimeTube to work properly. You can also install them manually
with pip or similar tools if you prefer. 

##### Running Animetube:
Although AnimeTube aims to be an api allowing anyone to create any sort of front-end 
for it, it also comes with a very simple command line interface located in **src/main.py**

**NOTE:** At this point in time if you do use **src/main.py** you'll need to have vlc player installed

##### TODO:

* Add more sites to parse
* ~~Add parsers for hosts other than trollvideo~~
* Program still needs a lot more structure 
* Add config file (for preferences) capability
    
