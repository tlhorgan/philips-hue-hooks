# Philips Hue Hooks

This is an experimental attempt to simulate a webhook behavior when motion is detected or when a light switch is pressed, by continuously polling the sensor status and sending a POST webhook when there is change.

**BETA alert**: APIs are subject to change!

## Initialisation

### Identify the bridge address
You can use a network discovery tool such as `nmap`.

### Create a username
- Navigate to `http://<hostname>/debug/clip.html`
- POST `/api`, with body `{"devicetype":"insert_device_type_here"}`
- It will fail, press the button on the Hue hub and try again.
- It will succeed, and return a username. Note it.

### Identify the sensor(s)
- Navigate to `http://<hostname>/debug/clip.html`
- GET `/api/<username>/sensors`, and note the sensor ID corresponding to your motion detection sensor.

### More info
For more information, you can check Philips' [getting started](https://www.developers.meethue.com/documentation/getting-started) docs.

## Run

### Test
```
./hook.sh --host=<host> \
    --username=<username> \
    --sensor_ids=<sensor_ids>
```

For example,

```
./hook.sh --host=192.168.0.16 \
    --username=DjKbc3uiIPf7xleIw08FD3UR7V1vzJGNnfRcDbFv \
    --sensor_ids=9
```

Check that sensor movements are logged on stdout.

### Plug your webhook

Build a hook target that listens to POST requests. The POST body will be:
```
{
    "id": <sensor_id>,
    "state": <new_state>
}
```

where `new_state` is:
- for a motion detector: [on, off, turning_off]
- for a light switch: [on, brightness_up, brightness_down, off]


Then start the motion poller:
```
./hook.sh --host=<host> \
    --username=<username> \
    --sensor_ids=<sensor_ids> \
    --target=<hook_target>
```

For example,

```
./hook.sh --host=192.168.0.16 \
    --username=DjKbc3uiIPf7xleIw08FD3UR7V1vzJGNnfRcDbFv \
    --sensor_ids=9 \
    --target=http://localhost:8080
```