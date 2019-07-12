# Welcome to the documentation page of LittlevGL

LittlevGL is a free and open-source graphics library providing everything you need to create an embedded GUI with easy-to-use graphical elements, beautiful visual effects and a low memory footprint.

Website: https://littlevgl.com/   
Main repository: https://github.com/littlevgl/lvgl  

The documentation is available in:
- **HTML** format: http://docs.littlevgl.com/

# How to use this documentation

The documentation is written in [Markdown](https://en.wikipedia.org/wiki/Markdown). There are many converter tools available to generate HTML or PDF from Markdown files. 

## Rebuild the documentation

The following directions are given for Ubuntu, but should also be useful as a general guide. They assume that https://github.com/littlevgl/lvgl is cloned in a folder named `lvgl`, and https://github.com/littlevgl/docs is beside it in another folder named `docs`. The paths are not important (both folders can be located anywhere) but you may have to adjust these instructions slightly.

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


# Contributing 

Contributing is very welcome in this repository! 

## Translate existing pages
You can translate the existing documentation. Just copy the `md` files from the root folder to `locale/code/` where `code` is the abbreviation code of the language. For example `de` for German ans `fr` for French. See the full list [here](https://www.loc.gov/standards/iso639-2/php/code_list.php). 

You don't need to translate all the pages. Even one or two pages are welcome!

To push back your updates please create Pull request.

## Improve the documentation
If you find some missing information, typo or unclear parts, please add you fixes in a Pull request.
