# C++ D-Bus example

D-Bus client/server example in c++ using sdbus-c++.

### Dependency

* [sdbus-c++](https://github.com/Kistler-Group/sdbus-cpp)

### Building server / client

```shell
cd <server/client>
conan install . --output-folder=build --build=missing
meson setup --native-file build/conan_meson_native.ini . ./builddir
meson compile -C ./builddir
./builddir/<server/client>
```

or run `python run.py`

### License

```
Copyright 2023 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
