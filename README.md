# awtiCode
Code developed by and for Arba Minch Water Technology Institute (AWTI) staff. The raw code can be found on the repository [jddingemanse/awtiCodeDev](http://www.github.com/jddingemanse/awtiCodeDev) under the folder /code/, some corresponding data can be found under the folder /data/.

## About awtiCode
Development of code under repositories awtiCodeDev and awtiCode is an initiative to let some AWTI staff gain experience in coding by (trying to) write relevant code for their colleagues.

Some of the code is organized as functions under a package, that you can install in your preferred Python coding environment. This repository (awtiCode) contains the package code.

## Installation of awtiCode as package
First, make sure git is installed. In anaconda prompt:
```
conda install git
```
If git is installed, you can install awtiCode with:
```
pip install git+https://github.com/jddingemanse/awtiCode.git
```
If that was successful, you should be able to import awtiCode into your Python working environment.

## Using the package awtiCode
In your Python IDE (for example, Spyder or Jupyter Notebook):
```
import awtiCode
```
Under awtiCode, there are different modules:
- fillMissing: some functions to fill missing data;
- ftpChirps: some functions to communicate with the FTP server of CHIRPS data;
- mixedFileTypes: some functions to combine data of mixed file types, such as satellite and station data;
- tempAnimation: a function to create an animation based on a netCDF file.

For example, to use the function ftpChirpsExplore (under the module ftpChirps; to explore the directories and files available on the CHIRPS FTP server):
```
import awtiCode
awtiCode.ftpChirps.ftpChirpsExplore()
```
or, more efficiently:
```
from awtiCode.ftpChirps import ftpChirpsExplore
ftpChirpsExplore()
```
The package awtiCode is very much under development - by developing code for this repository and package, we are also learning to code ourselves. Current code might contain errors, and not yet all code is properly explained with comments or docstrings. If you run into any errors, please raise an issue on this repository. If things are unclear, please let us know as well.
