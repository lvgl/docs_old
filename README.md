# Welcome to the documentation's source of LVGL

This the source of LVGL's documentation avaialble on https://docs.lvgl.io

## Overview

### Tools
The documentation is craeted with Sphinx and RTD theme and with the use of several extensions. See below.

### Branches

There are the following branches:
- `master` Collection of the built docuementation for each version
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

### Improve the docs

As you read the documentation you might see some typos or unclear sentences. 
For typos and straightforward fixes, you can simply edit the file on GitHub. There is an `Edit on Github` link on the top right-hand corner of all pages.
Click it to see the file on GitHub, hit the Edit button, and add you fixes as described in [Pull request - From GitHub](https://docs.lvgl.io/latest/en/html/contributing/index.html#from-github) section.

Note that the documentation is also formatted in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 

### Translate the docs

If you have more free time you can even translate the documentation. The currently available languages are shown in the [locals](https://github.com/lvgl/docs/tree/latest/locales) folder.

If your chosen language is still not added, please write a comment [here](https://forum.lvgl.io/t/translate-the-documentation/238).

To add your translations:
- Find the *.po* in `<language_code>/LC_MESSAGES/<section_name>.po`. E.g. the widgets translated to German should be in `de/LC_MESSAGES/widgets.po`.
- Open a po file and fill the `msgstr` fields with the translation
- Send a [Pull request](https://docs.lvgl.io/latest/en/html/contributing/index.html#pull-request)

To display a translation in the public documentation page at least these sections should be translated:
- Get started: Quick overview
- Overview: Objects, Events, Styles
- Porting: System overview, Set-up a project, Display interface, Input device Interface, Tick interface
- 5 widgets of your choice

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

```sh
$ ls .
docs lvgl
$ pip install -U sphinx recommonmark commonmark breathe sphinx-rtd-theme
$ cd docs # IMPORTANT: note the two .. paths. The lvgl folder also has a folder inside it named docs.
$ rm xml/*
$ cp -a ../lvgl/docs/api_doc/xml/* xml/
$ cd en
$ make html
The HTML pages are in _build/html.
$
```
