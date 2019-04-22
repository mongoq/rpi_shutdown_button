# Raspberry Pi Shutdown Button

**Push to shut Raspberry Pi down ...**

![Push Button](https://static.thenounproject.com/png/509859-200.png)

---

**Implemented as a service: https://github.com/Cronixx/Raspberry-Systemd-Shutdown-Button-Service (Thanks to Jerry (!))**
**(100% CPU time fixed ...)**
**^ use this ;-)**

---


To sort:

PROBLEM: USES 100% CPU TIME

http://razzpisampler.oreilly.com/ch07.html

https://www.raspberrypi.org/forums/viewtopic.php?t=133665

https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up

https://maker-tutorials.com/raspberry-pi-mit-einer-bueroklammer-ausschalten-bzw-herunterfahren/

---

Start at Raspbian Startup by putting it in /etc/rc.local

In /etc/rc.local: /home/pi/projects/rpi_shutdown_button/rpi_shutdown_button.py

chmod +x /home/pi/projects/rpi_shutdown_button/rpi_shutdown_button.py

---

Pins 18 and GND - short them to force shutdown ...

---
Raspberry Pi 1
![Pinout](http://razzpisampler.oreilly.com/images/rpck_1101.png)

---

Raspberry Pi 2/3
![Pinout 2](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg)
