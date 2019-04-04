_Written for v5.1_

You can try out the Littlev Graphics Library **using only your PC** without any development board. Write a code, run it on the PC and see the result on the monitor. It is cross-platform: Windows, Linux and OSX are supported!

- Needs only few minutes setup
	
- Costs $0. No PCB cost and no pay for any software
	
- A TFT display is simulated and shown on the monitor of your PC
	
- The touch pad is replaced by your mouse
	
- The written code is portable, you can simply copy it when using an embedded hardware

#### Install Eclipse CDT

Eclipse CDT is C/C++ IDE. You can use other IDEs as well but in this tutorial the configuration for Eclipse CDT is shown.

Eclipse is a Java based software therefore be sure **Java Runtime Environment** is installed on your system.   

On Debian-based distros (e.g. Ubuntu): `sudo apt-get install default-jre`

You can download Eclipse's CDT from: [https://eclipse.org/cdt/](http://www.eclipse.org/downloads/). Start the installer and choose *Eclipse CDT* from the list.

#### Install SDL 2

The PC simulator uses the [SDL 2](https://www.libsdl.org/download-2.0.php) cross platform library to simulate a TFT display and a touch pad. 

##### Linux

On **Linux** you can easily install SDL2 using a terminal:

1. Find the current version of SDL2: `apt-cache search libsdl2 (e.g. libsdl2-2.0-0)`
2. Install SDL2: `sudo apt-get install libsdl2-2.0-0` (replace with the found version)
3. Install SDL2 development package: `sudo apt-get install libsdl2-dev`
4. If build essentials are not installed yet: `sudo apt-get install build-essential`

##### Windows

If you are using **Windows** firstly you need to install MinGW ([64 bit version](http://mingw-w64.org/doku.php/download)). After it do the following steps to add SDL2:

1. Download the development libraries of SDL.   
Go to [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) and download _Development Libraries: SDL2-devel-2.0.5-mingw.tar.gz_
2. Uncompress the file and go to _x86_64-w64-mingw32_ directory (for 64 bit MinGW) or to _i686-w64-mingw32_ (for 32 bit MinGW)
3. Copy _..._mingw32/include/SDL2_ folder to _C:/MinGW/.../x86_64-w64-mingw32/include_
4. Copy _..._mingw32/lib/_ content to _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. Copy _..._mingw32/bin/SDL2.dll_ to _{eclipse_worksapce}/pc_simulator/Debug/_.  Do it later when Eclipse is installed. 

Note: If you will use **Microsoft Visual Studio** instead of Eclipse then you don't have to install MinGW. 

##### OSX

On **OSX** you can easily install SDL2 with brew: `brew install sdl2`

If something is not working I suggest [this tutorial](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) to get started with SDL.

#### Pre-configured project

A pre-configured graphics library project (based on the latest release) is always available in PC simulator project. You can find it on [GitHub](https://github.com/littlevgl/proj_pc) or on the [Download](https://littlevgl.com/download) page. The project is configured for Eclipse CDT. 

#### Add the pre-configured project to Eclipse CDT

Run Eclipse CDT. It will show a dialogue about the **workspace path**. Before accepting it check that path and copy (and unzip) the downloaded pre-configured project there. Now you can accept the workspace path. Of course you can modify this path but in that case copy the project to that location.

Close the start up window and go to **File-&gt;Import** and choose **General-&gt;Existing project into Workspace**. **Browse the root directory** of the project and click **Finish**

On **Windows** you have to do two additional things:

- Copy the **SDL2.dll** into the project's Debug folder 
- Righ click on the project -&gt; Project properties -&gt; C/C++ Build -&gt; Settings -&gt; Libraries -&gt; Add ... and add _mingw32_ above SDLmain and SDL. (The order is important: mingw32, SDLmain, SDL)

#### Compile and Run

Now you are ready to run the Littlev Graphics Library on your PC. Click on the Hammer Icon on the top menu bar to Build the project. If you have done everything right you will not get any errors. Note that on some systems additional steps might be required to "see" SDL 2 from Eclipse but in most of cases the configurtions in the downloaded project is enough.

After a success build click on the Play button on the top menu bar to run the project. Now a window should appear in the middle of your screen.

Now everything is ready to use the Littlev Graphics Library in the practice or begin the development on your PC.

#### Next step

To create your first LittlevGL GUI you should read the pages below [[Porting]] in the sidebar.