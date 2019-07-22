```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/get-started/pc-simulator.md
```
# PC上的模拟器


你可以通过**使用你的PC**来尝试LittlevGL而无需任何开发板，你可以在PC上编写、运行代码和在监视器上查看运行结果。这种方式是跨平台的，Windows, Linux 和 OSX都支持。
这些代码都是可移植的，你可以轻易的复制运行到你的嵌入式硬件设备上。

同样的，模拟器也对反馈bug非常有帮助，因为它意味着每个用户的通用平台，所以最好在模拟器上用你的代码复现bug反馈到[论坛](https://forum.littlevgl.com)。

## 选择一个IDE

模拟器已经一直到多个IDE中，选择你最喜欢的IDE，阅读GitHub上的README，下载并在IDE上加载。

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

下面详细地描述了Eclipse CDT的配置指南

## 配置 Eclipse CDT

### 安装 Eclipse CDT

Eclipse CDT 是 C/C++ IDE，你也可以使用其他IDE，但在这个教程里我们呈现如何配置Eclipse CDT

Eclipse 是基于Java的软件，因此请确保 **Java 运行时环境（JRE）** 已经安装在你的系统上

在类Debian发行版上运行 (如：Ubuntu): `sudo apt-get install default-jre`

你可以从这里下载Eclipse's CDT: [https://eclipse.org/cdt/](http://www.eclipse.org/downloads/)，运行安装器从列表中选择 *Eclipse CDT*

### 安装 SDL 2

PC模拟器使用  [SDL 2](https://www.libsdl.org/download-2.0.php) 跨平台库来模拟 TFT 显示设备和触摸板。 

#### Linux
在 **Linux**  上你可以通过终端简单的安装SDL2：

1. 找到当前的SDL2版本: `apt-cache search libsdl2 (例如 libsdl2-2.0-0)`
2. 安装 SDL2: `sudo apt-get install libsdl2-2.0-0` (替代你找到的版本)
3. 安装SDL2开发包: `sudo apt-get install libsdl2-dev`
4. 如果基本编译库build essentials尚未安装: `sudo apt-get install build-essential`

#### Windows
如果你使用的是 **Windows** 首先你需要安装 MinGW ([64 位版本](http://mingw-w64.org/doku.php/download))，然后再按以下步骤安装SDL2：

1. 下载SDL的开发库   
前往 [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) 并 _下载库: SDL2-devel-2.0.5-mingw.tar.gz_
2. 解压并前往 _x86_64-w64-mingw32_ 文件夹(64 位的MinGW) 或 _i686-w64-mingw32_ ( 32 位的MinGW)
3. 复制 _..._mingw32/include/SDL2_ 文件夹到 _C:/MinGW/.../x86_64-w64-mingw32/include_
4. 复制_..._mingw32/lib/_ 中的内容到 _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. 复制_..._mingw32/bin/SDL2.dll_ 到_{eclipse_worksapce}/pc_simulator/Debug/_，请在Eclipse完成安装后执行

请注意：如果你使用的是 **Microsoft Visual Studio**而不是 Eclipse，那么你不需要安装 MinGW. 

#### OSX
你可以容易的通过brew在 **OSX** 上安装SDL2 ：`brew install sdl2`

如果没有用我建议查看[这个教程](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) 来开始使用SDL。

### 预配置项目

一个预配置的图形库项目（基于最新的版本）总是可用
你可以在 [GitHub](https://github.com/littlevgl/proj_pc) 或 [下载](https://littlevgl.com/download) 页面中找到它
(这个项目是为Eclipse CDT配置的) 

### 添加预配置项目到Eclipse CDT

运行Eclipse CDT，他会显示一个关于 **workspace path**的对话框，在接受之前复制 (并解压) 已下载好的预配置项目到上面的路径中，现在你可以接受这个workspace path。当然你也可以修改这个路径并复制项目到你自定义的路径中

关闭开始窗口并前往 **File-&gt;Import** 选择 **General-&gt;Existing project into Workspace**. **选择项目根目录** 并点击 **Finish**

在 **Windows** 你必须做这两件额外的事：

- 复制 **SDL2.dll** 到项目的Debug目录
- 右击项目的 -&gt; Project properties -&gt; C/C++ Build -&gt; Settings -&gt; Libraries -&gt; Add ... 并在 _mingw32_ 上添加 SDLmain 和 SDL。 (这个顺序非常重要: mingw32, SDLmain, SDL)

### 编译并运行

Now you are ready to run the LittlevGL Graphics Library on your PC. Click on the Hammer Icon on the top menu bar to Build the project. If you have done everything right you will not get any errors. Note that on some systems additional steps might be required to "see" SDL 2 from Eclipse but in most of cases the configurations in the downloaded project is enough.

在编译成功后点击在上方菜单栏中Play按钮来运行项目，现在一个窗口应该出现在你的屏幕中央

现在所有东西已经准备好，你可以开始在你PC上实践使用LittlevGL图形库了。
