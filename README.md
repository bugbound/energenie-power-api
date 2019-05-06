# About energenie-power-api
A basic Python Flask based API to turn Energenie power sockets on or off using Energenie pi hat attachment hardware.
The API listens for JSON post requests over http on port 7000.

# Hardware
https://www.amazon.co.uk/dp/B00T9JPANU/?ref=idea_lv_dp_ov_d - Energenie ENER010-PI Radio Transmitter PCB and 4 Gang RF Extension Lead 

# Calling the API
Turn socket one on:
```
curl --data '{"socket": 1, "power": true}' -H "Content-Type: application/json" http://HOSTIP:7000/api/power -X POST
```

Turn socket one off:
```
curl --data '{"socket": 1, "power": false}' -H "Content-Type: application/json" http://HOSTIP:7000/api/power -X POST
```

# Remote Install
To install dependencies:
```
fab setup --host <HOSTIP> --user pi
```
Copy and run the power api :
```
fab deploy --host <HOSTIP> --user pi
```


  
