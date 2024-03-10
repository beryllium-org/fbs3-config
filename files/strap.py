try:
    mkdir(path.join(root, "etc/camera.d"))
except FileExistsError:
    pass

shutil.copy("config.toml", path.join(root, "etc/camera.d", "config.toml"))

try:
    mkdir(path.join(root, "etc/camera.d/presets"))
except FileExistsError:
    pass

shutil.copy("high.toml", path.join(root, "etc/camera.d/presets", "high.toml"))

for i in ["axp313a.lja", "axp313a.py"]:
    shutil.copy(i, path.join(root, "bin", i))

shutil.copy("axp313a.man", path.join(root, "usr/share/man", "axp313a.man"))
