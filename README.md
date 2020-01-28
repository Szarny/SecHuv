<img src="./resource/top_banner.png" alt="SecHuv-logo" style="width: 650px" />

[![](http://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

# SecHuv
Security Hub for Human-vulnerabilities.

## System Configuration
|System|Description|
|:-:|:-|
|SecHuv:CHVE|Common Human Vulnerabilities and Exposures; The central intelligence repository for the SecHuv system.|
|SecHuv:Viewer|Web system for viewing cases stored in the SecHuv system.|
|SecHuv:Web|Browser extension to detect malicious web sites.|
|SecHuv:Mail|Tool to detect malicious e-mails.|
|SecHuv:Heart|Chatbot for consulting about attacks that exploit human-vulnerabilities.|

## Usage
You can starts up the server environment easily with *Docker*.
```
$ cd docker
$ ./docker-build.sh
$ docker-compose up
```


Then, the server starts with the following `IP:port`.

|Server|`IP:port`|
|:-:|:-:|
|SecHuv:CHVE|`http://localhost:8080/*`|
|SecHuv:Viewer|`http://localhost:8000/*`|
|SecHuv:Heart|`http://localhost:8000/heart`|
|Swagger UI|`http://localhost:5000/`|
|Swagger Editor|`http://localhost:5001/`|