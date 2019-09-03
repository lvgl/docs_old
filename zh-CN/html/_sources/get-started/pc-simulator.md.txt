```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/get-started/pc-simulator.md
```
# PC上的模拟器


You can try out the LittlevGL **using only your PC** (i.e. without any development boards). The LittlevGL will run on a simulator environment on the PC where anyone can write and experiment the real LittlevGL applications.

Simulator on the PC have the following advantages:
- Hardware independent - Write a code, run it on the PC and see the result on the PC monitor.
- Cross-platform - Any Windows, Linux or OSX PC can run the PC simulator.  
- Portability - the written code is portable, which means you can simply copy it when using an embedded hardware.
- Easy Validation - The simulator is also very useful to report bugs because it means common platform for every user. So it's a good idea to reproduce a bug in simulator and use the code snippet in the [Forum](https://forum.littlevgl.com).

## 选择一个IDE

The simulator is ported to various IDEs (Integrated Development Environments). Choose your favorite IDE, read its README on GitHub, download the project, and load it to the IDE.

```eval_rst
.. raw:: html

  <table style="width:100%">
  <thead>
  <tr>
  <th>Eclipse</th>
  <th>CodeBlocks</th>
  <th>Visual Studio</th>
  <th>PlatformIO</th>
  <th>Qt Creator</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a href="https://github.com/littlevgl/pc_simulator_sdl_eclipse"><img src="https://littlevgl.com/logo/ide/eclipse.jpg"></a> </td>
  <td><a href="https://github.com/littlevgl/pc_simulator_win_codeblocks"><img src="https://littlevgl.com/logo/ide/codeblocks.jpg"></a></td>
  <td><a href="https://github.com/littlevgl/visual_studio_2017_sdl_x64"><img src="https://littlevgl.com/logo/ide/visualstudio.jpg"></a></td>
  <td><a href="https://github.com/littlevgl/pc_simulator_sdl_platformio"><img src="https://littlevgl.com/logo/ide/platformio.jpg"></a></td>
  <td><a href="https://blog.littlevgl.com/2019-01-03/qt-creator"><img src="https://littlevgl.com/logo/ide/qtcreator.jpg"> </a></td>
  </tr>

  <tr>
  <td>Cross-platform<br>with SDL 
  </td><td>Native Windows  </td>
  <td>Cross-platform<br>with SDL  </td>
  <td>Cross-platform<br>with SDL </td>
  <td>Cross-platform<br>with SDL  </td>
  </tr>
  </tbody></table>
```


You can use any IDEs for the development but, for simplicity, the configuration for Eclipse CDT is focused in this tutorial.
The following section describes the set-up guide of Eclipse CDT in more details.

**Note: If you are on Windows, it's usually better to use the Visual Studio or CodeBlocks projects instead. They work out of the box without requiring extra steps.**

## 配置 Eclipse CDT

### 安装 Eclipse CDT

[Eclipse CDT](https://eclipse.org/cdt/) is a C/C++ IDE.

Eclipse 是基于Java的软件，因此请确保 **Java 运行时环境（JRE）** 已经安装在你的系统上

在类Debian发行版上运行 (如：Ubuntu): `sudo apt-get install default-jre`

Note: If you are using other distros, then please refer and install 'Java Runtime Environment' suitable to your distro.

You can download Eclipse's CDT from: [https://www.eclipse.org/cdt/downloads.php](https://www.eclipse.org/cdt/downloads.php). Start the installer and choose *Eclipse CDT* from the list.

### 安装 SDL 2

PC模拟器使用  [SDL 2](https://www.libsdl.org/download-2.0.php) 跨平台库来模拟 TFT 显示设备和触摸板。 

#### Linux
在 **Linux**  上你可以通过终端简单的安装SDL2：

1. 找到当前的SDL2版本: `apt-cache search libsdl2 (例如 libsdl2-2.0-0)`
2. 安装 SDL2: `sudo apt-get install libsdl2-2.0-0` (替代你找到的版本)
3. 安装SDL2开发包: `sudo apt-get install libsdl2-dev`
4. 如果基本编译库build essentials尚未安装: `sudo apt-get install build-essential`

#### Windows
If you are using **Windows** firstly you need to install MinGW ([64 bit version](http://mingw-w64.org/doku.php/download)). After installing MinGW, do the following steps to add SDL2:

1. 下载SDL的开发库   
前往 [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) 并 _下载库: SDL2-devel-2.0.5-mingw.tar.gz_
2. 解压并前往 _x86_64-w64-mingw32_ 文件夹(64 位的MinGW) 或 _i686-w64-mingw32_ ( 32 位的MinGW)
3. 复制 _..._mingw32/include/SDL2_ 文件夹到 _C:/MinGW/.../x86_64-w64-mingw32/include_
4. 复制_..._mingw32/lib/_ 中的内容到 _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. 复制_..._mingw32/bin/SDL2.dll_ 到_{eclipse_worksapce}/pc_simulator/Debug/_，请在Eclipse完成安装后执行

Note: If you are using **Microsoft Visual Studio** instead of Eclipse then you don't have to install MinGW. 

#### OSX
你可以容易的通过brew在 **OSX** 上安装SDL2 ：`brew install sdl2`

If something is not working, then please refer [this tutorial](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) to get started with SDL.

### 预配置项目

A pre-configured graphics library project (based on the latest release) is always available to get started easily. 
You can find the latest one on [GitHub](https://github.com/littlevgl/proj_pc) or on the [Download](https://littlevgl.com/download) page. 
(Please note that, the project is configured for Eclipse CDT). 

### 添加预配置项目到Eclipse CDT

Run Eclipse CDT. It will show a dialogue about the **workspace path**. Before accepting the path, check that path and copy (and unzip) the downloaded pre-configured project there. After that, you can accept the workspace path. Of course you can modify this path but, in that case copy the project to the corresponding location.

关闭开始窗口并前往 **File-&gt;Import** 选择 **General-&gt;Existing project into Workspace**. **选择项目根目录** 并点击 **Finish**

在 **Windows** 你必须做这两件额外的事：

- 复制 **SDL2.dll** 到项目的Debug目录
- 右击项目的 -&gt; Project properties -&gt; C/C++ Build -&gt; Settings -&gt; Libraries -&gt; Add ... 并在 _mingw32_ 上添加 SDLmain 和 SDL。 (这个顺序非常重要: mingw32, SDLmain, SDL)

### 编译并运行

Now you are ready to run the LittlevGL Graphics Library on your PC. Click on the Hammer Icon on the top menu bar to Build the project. If you have done everything right, then you will not get any errors. Note that on some systems additional steps might be required to "see" SDL 2 from Eclipse but, in most of cases the configurations in the downloaded project is enough.

After a success build, click on the Play button on the top menu bar to run the project. Now a window should appear in the middle of your screen.

现在所有东西已经准备好，你可以开始在你PC上实践使用LittlevGL图形库了。
