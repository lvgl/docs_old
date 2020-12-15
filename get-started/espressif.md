```eval_rst
.. include:: /header.rst 
:github_url: |github_link_base|/get-started/espressif.md
```

# Espressif (ESP32)
LVGL includes a Kconfig file so it can be directly used as an ESP-IDF v4 component.

# Get the LVGL library

When using the ESP-IDF v4 framework from Espressif you can add external libraries as "components". This components can be located inside a directory named "components" on your project root directory.

When your project is a git repository you can include LVGL as a git submodule:

```c
git submodule add https://github.com/lvgl/lvgl.git components/lvgl
```

The above command will clone LVGL's main repository into the `components/lvgl` directory. LVGL includes a `CMakeLists.txt` file that sets some configuration options so you can use LVGL right away.

When you are ready to configure LVGL launch the configuration menu with `idf.py menuconfig` on your project root directory.
