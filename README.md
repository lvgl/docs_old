# Welcome to the documentation page of LittlevGL

LittlevGL is a free and open-source graphics library providing everything you need to create an embedded GUI with easy-to-use graphical elements, beautiful visual effects and a low memory footprint.

Website: https://littlevgl.com/   
Main repository: https://github.com/littlevgl/lvgl  

The documentation is available in:
- **HTML** http://docs.littlevgl.com/  
- **PDF** [LittlevGL English.pdf](https://docs.littlevgl.com/en/html/_downloads/6c5a7f415f5012e697cd0b80e864c8a6/LittlevGL.pdf)

The documentation is being translated into several languages. You can select between them in the top of the Welcome page.

## Contributing

If you would like to contribute to LittlevGL the documentation is the best place to start.

### Fix typos, add missing parts

If you find a typo, an obscure sentence or something which is not explained well enough in the **English** documentation click the *"Edit on GitHub"* button in the top right corner and fix the issue by sending a Pull Request.

### Translate the documentation

If you have time and intereset you can translate the documentation to your native language or any language you speak. 
You can join others to work on an already existing language or you can start a new one.  

To translate the documentation we use [Zanata](https://zanata.org) which is an online translation platform. 
You will find the LittlevGL project here: [LittlevGL on Zanata](https://translate.zanata.org/iteration/view/littlevgl-docs/v6.0-doc1?dswid=3430) 

To get started you need to:
- register at [Zanata](https://zanata.org) which is an online translation platform.  
- comment to [this post](https://forum.littlevgl.com/t/translate-the-documentation/238?u=kisvegabor)
- tell your username at *Zanata* and your selected language(s) to get permission the edit the translations

Note that a translation will be added to the documentation only if at least the [Porting section](https://docs.littlevgl.com/en/html/porting/index.html) is translated.

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
