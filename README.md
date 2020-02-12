# GPIO Shutdown For Raspberry Pi

## About

This is a small script, intended to be run from systemd, that will
shutdown the Pi if it detects a state change on a GPIO pin.  This
would be caused by a button or switch that ties a GPIO pin either to
ground or +5V.

Note: The pin is identified by the *GPIO Number* not the board number

The script listens for a state change on the specified pin.  The
states are either *RISING* or *FALLING*.

* *FALLING*: The button ties the pin to ground. In this case, the internal resistor will be set to PULLUP.

* *RISING*: The button ties the pin to +5V. In this case, the internal resister will be set to PULLDOWN.

There are hard-coded defaults in the script.  In the git repository,
the script has a default state of FALLING and the default pin is 21.
Pin 21 is the last pin on the Pi and is next to a ground pin on the
next row.  It's a convinient place to attach the button.

The script can be configured in one of three ways:

1. *Command line args*.  The pin is the first arg.  The state
("FALLING" or "RISING") is the second arg.  If no state, or no pin or
state is specified, then the values will either be the hard-coded
defaults or those values that are defined as below.  The command line
args take precedence over the methods 2 or 3.

2. *Environment Variables*. See `examples/systemd/listen-for-shutdown.service`

3. *Environment File*. See `examples/default/listen-for-shutdown`

## Requirements:

* Python3
* RPi.GPIO from PyPi

## Installation

Place listen-for-shutdown.py somewhere from where
systemd can run it, such as `/usr/local/bin`.

Modify `examples/systemd/listen-for-shutdown.service` and place it in `/etc/systemd/system`

If using an environment file, modify
`examples/default/listen-for-shutdown` and place it where appropriate
for your OS.  In Raspbian this is `/etc/default/`.

    sudo systemctl enable listen-for-shutdown.service
    sudo systemctl start listen-for-shutdown.service
    sudo systemctl status listen-for-shutdown.service

If the service failed, use `journalctl` to investigate:
    sudo journalctl -xe -u listen-for-shutdown.service
