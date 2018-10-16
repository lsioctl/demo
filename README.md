# demo

App to be tested with cicdinfra

## test the availability of the update

* launch for example:
```
watch -n 0.5 curl http://127.0.0.1:8082/ -w "\n"
```

Note: not localhost, Docker Swarm loadbalancer do not understand IPv6

* update the code

