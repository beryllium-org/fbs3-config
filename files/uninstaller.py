be.based.run("rm /etc/camera.d/config.toml /etc/camera.d/presets/high.toml /bin/axp313a.lja /bin/axp313a.py /usr/share/man/axp313a.man /boot/boot.d/10-fbs3I2C.lja")
be.based.run("rmdir /etc/camera.d/presets")
be.based.run("rmdir /etc/camera.d")

be.api.setvar("return", "0")
