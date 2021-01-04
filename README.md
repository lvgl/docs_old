# Welcome to the documentation's source of LVGL

This the source of LVGL's documentation avaialble on https://docs.lvgl.io

## Overview

### Tools
The documentation is craeted with Sphinx and RTD theme and with the use of several extensions. See below.

### Branches

There are the following branches:
- `master` Collection of the built documentation for each version
- `latest` Documentation for the `master` branch of lvgl. It contains the last features available for testing.
- `dev` Documentation for the `dev` branch of lvgl. These features are not stabel and might change. 
- `release/vX` Documentation for the `release/vX` branch of lvgl (`X` stands for major relases of lvgl). These are the last relased stable versions.

On every release (first and third Tuesday of every month)
1. Rebuild and publish `latest`
2. Merge `latest` to `release/vX`
3. Merge `latest` to `dev`
4. Merge `dev` to `latest`
5. Rebuild and publish all 3 branches

## Contributing

As you read the documentation you might see some typos or unclear sentences. 
For typos and straightforward fixes, you can simply edit the file on GitHub. There is an `Edit on Github` link on the top right-hand corner of all pages.
Click it to see the file on GitHub, hit the Edit button, and add you fixes as described in [Pull request - From GitHub](https://docs.lvgl.io/latest/en/html/contributing/index.html#from-github) section.

Note that the documentation is also formatted in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 

## Rebuild the documentation

### Official rebuilds

The documentation is rebuild on every release of lvgl (first and third Tuesday of every month).

### Build locally

The following directions are given for Ubuntu, but should also be useful as a general guide. They assume that https://github.com/lvgl/lvgl is cloned in a folder named `lvgl`, and https://github.com/lvgl/docs is beside it in another folder named `docs`. The paths are not important (both folders can be located anywhere) but you may have to adjust these instructions slightly.

To rebuild the API documentation, you need [Doxygen](http://www.doxygen.nl/).

```sh
$ ls .
docs lvgl
$ sudo apt install doxygen
$ cd lvgl/scripts
$ doxygen Doxyfile
```

The documentation is compiled into HTML or another form using [Sphinx](https://www.sphinx-doc.org). In order to get started Sphinx and some other components need to be installed on your system. 


Install dependencies:
```sh
$ pip install -U sphinx recommonmark commonmark breathe sphinx-rtd-theme sphinx-markdown-tables sphinx-sitemap
```

Get the `docs` and `lvgl` repositories
```sh
$ git clone https://github.com/lvgl/docs.git --recurse-submodules 
$ git clone https://github.com/lvgl/lvgl.git
$ ls .
docs lvgl
```

Enter to the `docs` folder and change branch:
```sh
$ cd docs
$ git checkout latest --
$ git submodule update --init
```

Update the API reference of the `docs` from `lvgl` (optional):
```sh
$ rm xml/*
$ cd ../lvgl/scripts
$ doxygen -u
$ cd ../../docs
$ cp -a ../lvgl/docs/api_doc/xml/* xml/
```

Built HTML
```sh
$ make html
```

The HTML pages are in the `html`.
