import os
import platform

if platform.system() in ("Windows", "Darwin"):
    print(f"SKIPPED TEST BECAUSE MESON IS NOT INSTALLED IN WINDOWS AND MACOS YET.")
    exit(0)

application = "client"

os.system("conan install . --output-folder=build --build=missing")
os.system("meson setup --native-file build/conan_meson_native.ini . ./builddir")
os.system("meson compile -C ./builddir")
os.system("./builddir/" + application)
