# Cloud Setup
We have created two VM for this process

- **52.xxx.xx.134:** VM on which openwhisk resides

- **52.xxx.xx.131:** VM on which our sanity controller resides

### Background
Openwhisk has already been setup in the 1st VM. Sanity would ideally have all the components(Couchdb, minio and kafka). 
We have to write actions and triggers to invoke through sanity to perform the cloud functions operations.
First we need to install wsk cli to configure command line interface for openwhisk.
Steps to do that:
1)	https://openwhisk.ng.bluemix.net/cli/go/download/linux/amd64/ Download binaries from this site
2)	Go to downloads folder and modify permissions for wsk file using terminal
$ chmod +x ./wsk
3)	Move wsk to use/local/bin folder using terminal. This will add wsk to the PATH
$ sudo mv wsk /usr/local/bin
4)	Test this using following command:
$ wsk –help
Now having the wsk setup, we need to interact with ngnix server of openwhisk. To do that, we need to configure API Host.
In our case, we want to run openwhisk functions to interact with the other VM, else we might come up with this error
“Cannot connect to API host”

With this command, you can set your API host:
wsk property set –apihost <Host IP>
 
The next step is to add SSL to our environment
wsk property set --auth 23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP

This is the public key for openwhisk.

Once you do this, wsk is ready to invoke actions
1)	Write the program logic
2)	Create actions 
wsk –i action create <name> <file name>
3)	Invoke actions
wsk action invoke <name> --blocking --param name <actions name>
 
![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/openwhisk.png)
 
