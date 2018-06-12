# ROS Code 1.0 Documentation

!!! failure "Deprecation Notice"

    ROS Code 1.0 is deprecated and is not recommended for use in production. However, the `ros.py` file still exists but in a different name: `syntax.py`

!!! warning "Inaccurate Information"

    The following content has been imported directly from the old documentation with little to no modification. Be aware that the information may not be accurate.

### Navigation:

[Home](#home)
 \|
[Licence](#ros-code-license)
 \|
[Download](#download-and-install-ros-code)
 \|
[Enable](#enable-ros-code-in-python)
 \|
[Build Status](#build-status)
 \|
[Troubleshooting](#troubleshooting)
 \|
[Watch Video](https://youtu.be/yGWcIwSZfJM?t=10s)

* * *

## Home

#### Explore ROS Code

##### The Easiest Way To Code

| | |
|:--:|:--:|
|![The Code Icon](legacy-images/code.png)|Open Source: This project is open source and the stable version is kept bug-free.|
|![An Image Of A Flag](legacy-images/flag.png)|Our Goal: Our goal is to make it easier for people to code in python with a single library.|
|![The Copyright Symbol](legacy-images/copyright.png)|Copyright: This project is licenced under the [Apache Licence 2](https://www.ros-code.ga/Licence).|
|![The Download Logo](legacy-images/download.png)|Download: Our fast and secure download servers will quickly download the installer.|
|![An Image Of A Cog](legacy-images/setup.png)|Setup And Install: Our express and pup-free installer will quickly install everything for you.|
|![The Bug Icon](legacy-images/bug.png)|Bugs: If you find a bug, you can easily report it at our [Github Page](https://github.com/Richienb/ROS-Code/issues).|

| | | | | | |
|:--:|:--:|:--:|:--:|:--:|:--:|
|Build Status|Issues|Forks|Stars|License|Version|
| [![Build Status](https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge)](https://travis-ci.org/Richienb/ROS-Code) | [![Current Issues](https://img.shields.io/github/issues/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/issues) | [![Current Forks](https://img.shields.io/github/forks/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/network) | [![Current Stars](https://img.shields.io/github/stars/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/stargazers) | [![Current License](https://img.shields.io/github/license/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/blob/master/LICENSE) | [![Current Release](https://img.shields.io/github/release/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/releases) |

## Build Status

#### Remember to check this before downloading the latest commit

### Current Build Status Via Travis:

[![Build Status](https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge)](https://travis-ci.org/Richienb/ROS-Code)

[View Travis Build Status Site](https://travis-ci.org/Richienb/ROS-Code)

### Embed The Build Status In Your Projects:

Image URL:

    https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge

Markdown:

```markdown
[![Build Status](https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge)](https://travis-ci.org/Richienb/ROS-Code)
```

reStructuredText:

    .. image:: https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge   :alt: Build Status  :target: https://travis-ci.org/Richienb/ROS-Code

AsciiDoc:

```asciidoc
image:https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge["Build Status",link="https://travis-ci.org/Richienb/ROS-Code"]
```

* * *

## Download And Install ROS Code

#### For all platforms running Python 3.x

### Find Your OS Below:

#### Windows:

### Download The Installer By Clicking The Button Below:

[![Download For Windows](https://img.shields.io/badge/Download-For%20Windows-3F51B5.svg?style=for-the-badge)](http://www.mediafire.com/file/yr8lt1njilkor22/ROS+Code+File+Fetcher.exe)

By clicking **Download For Windows** you will download the ROS Code Installer Version 1.1

[Download Version 1.0](https://download1339.mediafire.com/es7v2ckb31hg/n0z123y7buowlvi/ROS+Code+File+Fetcher.exe)

##### How To Use:

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

        ##### What build statuses mean:

        \|![build passing](https://img.shields.io/travis/rust-lang/rust.svg?maxAge=2592000&style=for-the-badge)\|![build failing](https://img.shields.io/teamcity/http/teamcity.jetbrains.com/s/bt345.svg?maxAge=2592000&style=for-the-badge)\|![build accessible](https://img.shields.io/magnumci/ci/96ffb83fa700f069024921b0702e76ff.svg?maxAge=2592000&style=for-the-badge)\|
        \|:---:\|:---:\|:---:\|
        |The latest commit passed the checks and is ready to be installed.|The latest commit **did not** pass the checks and you will experience runtime errors during runtime. Check back later or choose custom version.|The build status is currently unknown. Check back later or try refreshing the page.|

    2.  Using `Custom Version`

        Go to the official [Releases](https://github.com/Richienb/ROS-Code/releases) page or the [Release Tags](https://github.com/Richienb/ROS-Code/tags) page and choose a version to install.

        Type the version ID (For Example: `v1.4.5-release`) into the version textbox. The icon beside it should turn into a green tick. If not, check that you entered the correct version and try again. Otherwise, try another version.

2.  Press Install
    If you receive the following message: `Installation Successful`, then ROS Code has been successfully installed.

## Other OS:

-   Go to the official [Releases](https://github.com/Richienb/ROS-Code/releases) page or the [Release Tags](https://github.com/Richienb/ROS-Code/tags) page and choose a version to install.
-   Download the `.zip` or `.tar.gz` file
-   Find your Python 3.x installation directory
-   In the installation directory, navigate to `Lib` then `site-packages`
-   Extract the `ros.py` file from the `.zip` or `.tar.gz` file into the directory
-   You're done!

___

## Enable ROS Code

___
### Normal Method:

```python
import ros
ros.message_print('Hello World')
```

___
### Don't use the `ros` prefix:

```python
from ros import *
message_print('Hello World')
```

___
### Enable only a *specific* command:

```python
from ros import message_print
message_print('Hello World')
```
___
### Use a *different* command prefix other than `ros`

```python
import ros as tools
tools.message_print('Hello World')
```
___
### Enable only a *specific* command and *rename* it:

```python
from ros import message_print as message
message('Hello World')
```

___

## Troubleshooting

### ROS Code Error Code Explanations:
#### View The Explanations For All Error Codes Given By ROS Code.

|Error Code|Causing Functions|What Happened|How To Fix|
|:---------|:----------------|:------------|:---------|
|0001|throwerror(errortext)|An error was forced by the user.|Nothing. This error code (0001) must be provided so people know it was a custom-defined error.|
|0002|equation(operation, firstnum, secondnum)|Either the first number (firstnum) or the second number (secondnum) is not a number.|Ensure you are providing an actual number to the firstnum and secondnum variables.|
|0003|equation(operation, firstnum, secondnum)|The operation that you specified does not exist.|Ensure you use *plus*, *minus*, *multiply* or *divide* in the operation variable.|
|0004|randomstr(valuelist)|You haven't specified a list.|Make sure you've specified a list.|
|0005|debugstate(state)|You entered an invalid debug state.|Ensure you use *Enable* or *Disable* in the state variable.|
|0006|debug_varglobal() or debug_supresswarnings()|You tried to use a debug command when debug mode was disabled.|Enable debug mode by typing *ros.debugstate('Enable')*.|
|0007|dirtool(operation, directory)|The directory you specified doesn't exist.|Enter a directory that doesn't exist.|
|0008|dirtool(operation, directory) or convertsymbol(value, command)|An invalid operation has been entered.|Enter Either *exists* or *delete* in the operation variable.|
|0009|dirtool(operation, directory)|The directory you entered doesn't exist.|Enter a directory that exists.|
|0010|filedownload(source, destination)|An error has occurred while downloading the file.|Check the download URL.|
|0011|filedownload(source, destination)|The source or destination you entered is invalid.|Check the source or destination.|
|0012|file(operation, path)|The file you specified doesn't exist.|Check that the file actually exists.|
|0013|file(operation, path)|The file you specified already exists.|Check that the file doesn't exists.|
|0014|convertsymbol(value, command)|You entered an invalid symbol value.|Try another value.|
|0015|convertsymbol(value, command)|You entered an invalid symbol.|Try another symbol.|
|0016|randomnum(minimum, maximum)|You entered an invalid number.|Make sure the value is actually a number.|
|0017|openurl(url), newwindow(url) or newtab(url)|The URL was unable to open.|Check The URL or try another one.|

## ROS Code License

### Read the full ROS Code license here

#### Apache License | Version 2.0, January 2004 | <http://www.apache.org/licenses/>

## TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

### 1. Definitions.

"License" shall mean the terms and conditions for use, reproduction,
and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by
the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all
other entities that control, are controlled by, or are under common
control with that entity. For the purposes of this definition,
"control" means (i) the power, direct or indirect, to cause the
direction or management of such entity, whether by contract or
otherwise, or (ii) ownership of fifty percent (50%) or more of the
outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity
exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications,
including but not limited to software source code, documentation
source, and configuration files.

"Object" form shall mean any form resulting from mechanical
transformation or translation of a Source form, including but
not limited to compiled object code, generated documentation,
and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or
Object form, made available under the License, as indicated by a
copyright notice that is included in or attached to the work
(an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object
form, that is based on (or derived from) the Work and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship. For the purposes
of this License, Derivative Works shall not include works that remain
separable from, or merely link (or bind by name) to the interfaces of,
the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including
the original version of the Work and any modifications or additions
to that Work or Derivative Works thereof, that is intentionally
submitted to Licensor for inclusion in the Work by the copyright owner
or by an individual or Legal Entity authorized to submit on behalf of
the copyright owner. For the purposes of this definition, "submitted"
means any form of electronic, verbal, or written communication sent
to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems,
and issue tracking systems that are managed by, or on behalf of, the
Licensor for the purpose of discussing and improving the Work, but
excluding communication that is conspicuously marked or otherwise
designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity
on behalf of whom a Contribution has been received by Licensor and
subsequently incorporated within the Work.

* * *

### 2. Grant of Copyright License.

Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
copyright license to reproduce, prepare Derivative Works of,
publicly display, publicly perform, sublicense, and distribute the
Work and such Derivative Works in Source or Object form.

* * *

### 3. Grant of Patent License.

Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
(except as stated in this section) patent license to make, have made,
use, offer to sell, sell, import, and otherwise transfer the Work,
where such license applies only to those patent claims licensable
by such Contributor that are necessarily infringed by their
Contribution(s) alone or by combination of their Contribution(s)
with the Work to which such Contribution(s) was submitted. If You
institute patent litigation against any entity (including a
cross-claim or counterclaim in a lawsuit) alleging that the Work
or a Contribution incorporated within the Work constitutes direct
or contributory patent infringement, then any patent licenses
granted to You under this License for that Work shall terminate
as of the date such litigation is filed.

* * *

### 4. Redistribution.

You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without
modifications, and in Source or Object form, provided that You
meet the following conditions:

 (a) You must give any other recipients of the Work or
     Derivative Works a copy of this License; and

 (b) You must cause any modified files to carry prominent notices
     stating that You changed the files; and

 (c) You must retain, in the Source form of any Derivative Works
     that You distribute, all copyright, patent, trademark, and
     attribution notices from the Source form of the Work,
     excluding those notices that do not pertain to any part of
     the Derivative Works; and

 (d) If the Work includes a "NOTICE" text file as part of its
     distribution, then any Derivative Works that You distribute must
     include a readable copy of the attribution notices contained
     within such NOTICE file, excluding those notices that do not
     pertain to any part of the Derivative Works, in at least one
     of the following places: within a NOTICE text file distributed
     as part of the Derivative Works; within the Source form or
     documentation, if provided along with the Derivative Works; or,
     within a display generated by the Derivative Works, if and
     wherever such third-party notices normally appear. The contents
     of the NOTICE file are for informational purposes only and
     do not modify the License. You may add Your own attribution
     notices within Derivative Works that You distribute, alongside
     or as an addendum to the NOTICE text from the Work, provided
     that such additional attribution notices cannot be construed
     as modifying the License.

* * *

You may add Your own copyright statement to Your modifications and
may provide additional or different license terms and conditions
for use, reproduction, or distribution of Your modifications, or
for any such Derivative Works as a whole, provided Your use,
reproduction, and distribution of the Work otherwise complies with
the conditions stated in this License.

* * *

### 5. Submission of Contributions.

Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work
by You to the Licensor shall be under the terms and conditions of
this License, without any additional terms or conditions.
Notwithstanding the above, nothing herein shall supersede or modify
the terms of any separate license agreement you may have executed
with Licensor regarding such Contributions.

* * *

### 6. Trademarks.

This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor,
except as required for reasonable and customary use in describing the
origin of the Work and reproducing the content of the NOTICE file.

* * *

### 7. Disclaimer of Warranty.

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each
Contributor provides its Contributions) on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied, including, without limitation, any warranties or conditions
of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
PARTICULAR PURPOSE. You are solely responsible for determining the
appropriateness of using or redistributing the Work and assume any
risks associated with Your exercise of permissions under this License.

* * *

### 8. Limitation of Liability.

In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise,
unless required by applicable law (such as deliberate and grossly
negligent acts) or agreed to in writing, shall any Contributor be
liable to You for damages, including any direct, indirect, special,
incidental, or consequential damages of any character arising as a
result of this License or out of the use or inability to use the
Work (including but not limited to damages for loss of goodwill,
work stoppage, computer failure or malfunction, or any and all
other commercial damages or losses), even if such Contributor
has been advised of the possibility of such damages.

* * *

### 9. Accepting Warranty or Additional Liability.

While redistributing the Work or Derivative Works thereof, You may choose to offer,
and charge a fee for, acceptance of support, warranty, indemnity,
or other liability obligations and/or rights consistent with this
License. However, in accepting such obligations, You may act only
on Your own behalf and on Your sole responsibility, not on behalf
of any other Contributor, and only if You agree to indemnify,
defend, and hold each Contributor harmless for any liability
incurred by, or claims asserted against, such Contributor by reason
of your accepting any such warranty or additional liability.

> END OF TERMS AND CONDITIONS

* * *

> Copyright 2017 - 2018 Richie Bendall

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License [here](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
