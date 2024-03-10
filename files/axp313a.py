rename_process("axp313a")
vr("opts", be.api.xarg())
import AXP313A
vr("i2c", be.devices["gpiochip"][0].pin("I2C", force=True)())
vr("a", AXP313A.AXP313A(vr("i2c")))
if "c" in vr("opts")["o"]:
    vr("i2c", be.devices["gpiochip"][0].pin("I2C", force=True)())
    vr("a", AXP313A.AXP313A(vr("i2c")))
    if vr("opts")["o"]["c"] == "OV2640":
        be.api.setvar("return", str(int(not AXP313A.enable_camera(vr("a"), AXP313A.camera_voltages.OV2640))))
    elif vr("opts")["o"]["c"] == "OV7725":
        be.api.setvar("return", str(int(not AXP313A.enable_camera(vr("a"), AXP313A.camera_voltages.OV7725))))
    else:
        term.write("Invalid camera!")
        be.api.setvar("return", "1")
elif "d" in vr("opts")["o"]:
        AXP313A.disable_camera(vr("a"))
        be.api.setvar("return", "0")
else:
    term.write("Usage:\n    axp313a -c SENSOR_NAME\n    axp313a -d")
del AXP313A
