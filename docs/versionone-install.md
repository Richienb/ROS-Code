# Download And Install ROS Code

For all platforms running Python 3.x

### Find Your OS Below

#### Windows

Download The Installer By Clicking The Button Below:

[![Download For Windows](https://img.shields.io/badge/Download-For%20Windows-3F51B5.svg?style=for-the-badge)](http://www.mediafire.com/file/yr8lt1njilkor22/ROS+Code+File+Fetcher.exe)

By clicking **Download For Windows** you will download the ROS Code Installer Version 1.1

[Download Version 1.0](https://download1339.mediafire.com/es7v2ckb31hg/n0z123y7buowlvi/ROS+Code+File+Fetcher.exe)

##### How To Use

1.  Ensure you are connected to the internet throughout the installation process
2.  Download the install via the link above
3.  Launch the installer
4.  Type in your Python 3.x installation directory. Include `\Lib\site-packages` at the end. For example: `C:\Documents and Settings\All Users\Application Data\Python\Lib\site-packages`\*\`

5.  Choose the version of ROS Code you want to install in the combo box: _Canary - Latest Commit_ Or _Custom Version_

    Definitions:

    |Canary - Latest Commit|Custom Version|
    \|:--------------------:\|:------------:\|
    |Use The Latest Commit Of ROS Code|Use A Custom Version Of ROS Code Other Than Canary|

##### The following instructions depend on what option you chose in the last step

1.  Using `Canary - Latest Commit`

    1.  Check the build status. The current status is:

        [![Build Status](https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge)](https://travis-ci.org/Richienb/ROS-Code)

        ##### What build statuses mean

        \|![build passing](https://img.shields.io/travis/rust-lang/rust.svg?maxAge=2592000&style=for-the-badge)\|![build failing](https://img.shields.io/teamcity/http/teamcity.jetbrains.com/s/bt345.svg?maxAge=2592000&style=for-the-badge)\|![build accessible](https://img.shields.io/magnumci/ci/96ffb83fa700f069024921b0702e76ff.svg?maxAge=2592000&style=for-the-badge)\|
        \|:---:\|:---:\|:---:\|
        |The latest commit passed the checks and is ready to be installed.|The latest commit **did not** pass the checks and you will experience runtime errors during runtime. Check back later or choose custom version.|The build status is currently unknown. Check back later or try refreshing the page.|

    2.  Using `Custom Version`

        Go to the official [Releases](https://github.com/Richienb/ROS-Code/releases) page or the [Release Tags](https://github.com/Richienb/ROS-Code/tags) page and choose a version to install.

        Type the version ID (For Example: `v1.4.5-release`) into the version textbox. The icon beside it should turn into a green tick. If not, check that you entered the correct version and try again. Otherwise, try another version.

2.  Press Install
    If you receive the following message: `Installation Successful`, then ROS Code has been successfully installed.

## Other OS

-   Go to the official [Releases](https://github.com/Richienb/ROS-Code/releases) page or the [Release Tags](https://github.com/Richienb/ROS-Code/tags) page and choose a version to install.
-   Download the `.zip` or `.tar.gz` file
-   Find your Python 3.x installation directory
-   In the installation directory, navigate to `Lib` then `site-packages`
-   Extract the `ros.py` file from the `.zip` or `.tar.gz` file into the directory
-   You're done!
