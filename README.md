# energenie-power-api
A basic Python Flask based API to turn Energenie power sockets on or off using Energenie pi hat attachment hardware.

# Calling the API
Turn socket one on:
curl --data '{"socket": 1, "power": true}' -H "Content-Type: application/json" http://HOSTIP:7000/api/power -X POST

Turn socket one off:
curl --data '{"socket": 1, "power": false}' -H "Content-Type: application/json" http://HOSTIP:7000/api/power -X POST


# remote install
From the main directory run "fab setup --host <HOSTIP> --user pi" to install dependencies then run "fab deploy --host <HOSTIP> --user pi" to copy and start the power api. The api runs on port 7000.
  
