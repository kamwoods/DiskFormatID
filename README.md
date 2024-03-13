# DiskFormatID

More information is available in this blog post: http://digitalcontinuity.org/post/144268258748/floppy-disk-format-identifer-tool


This program is intended to help to identify floppy disk formats.  It takes a folder of http://www.Kryoflux.com stream files as input. It only works with linux and requires

* python >= 3.9
* pyqt6
* mount

Please support http://kryoflux.com/!

# Installation and Usage

Clone the repository or download all the files using the download zip button and extract them to a folder (not all are actually needed).

Optionally, create and start a Python virtual environment to install DiskFormatID with its own independent set of Python packages:

```
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip and ensure that the dependencies are installed:

```
pip install --upgrade pip
pip install pyqt6
pip install mount
```

In the DiskFormatID directory, build and install the program for all users as follows:

```
python setup.py build
sudo python setup.py install
```

Now, you can run the program as root from any location with:

```
sudo diskIDMain
```

(If you properly install DTC according to the instructions in the Kryoflux documentation then you may not need to run it as root).

The first time you start the program, you will see a warning that informs you a new settings file is being created. This settings file is located in the .diskFormatID directory within your home directory.

Click "choose formats" to select disk image formats to be created
Select input and output folders and specify the directory containing the Kryoflux DTC application. These settings (including selected formats) will be saved in "settings.json" 

NB: the program license must already have been agreed to by navigating to the dtc directory in a terminal window and running the GUI with:

```
java -jar kryoflux-ui.jar
```

Then accepting the prompt.

Choose how many concurrent dtc instances you want to run to create the disk images.
Click "create images" to use a local copy of the Kryoflux DTC program to create the image files from a folder containing folders of raw Kryoflux stream files. NB: the interface may lock up and not update the results for a indeterminate period of time. 

Click a button to mount the disk image files and get feedback on which files could be mounted. Check "delete unmountable" to delete the image files that couldn't be mounted. 

Click either of the "save results" buttons to save the results from the corresponding window to a file (extension will be added automatically). 

All created disk images will be have root permissions assigned, you may need to change that after using the program.

## License(s)

Unless otherwise indicated, software items in this respository are distributed under the terms of thne GNU General Public LIcense v3.0. See LICENSE file for additional details.

## Acknowledgements

DiskFormatID was developed by Euan Cochrane. Ported to Python 3 and Qt6 by Kam Woods.

