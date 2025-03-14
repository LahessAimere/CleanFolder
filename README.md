# CleanFolder 
<img src="https://www.hebergeur-image.com/upload/91.168.77.68-67aa9a112ff33.png" width="90" />

A script to keep computer files well organized by automatically sorting them based on their type (e.g., images, documents, archives, executables).

## Features :
- Automatically sorts files into categories such as "Images," "Documents," "Archives," and "Executables."
- Moves files into corresponding subfolders based on their extensions.
- Creates subfolders if they do not already exist.
- Ignores the script file itself, ensuring it won't be moved.
- Ignores README files to avoid sorting them.
- Supports both absolute paths and the current directory for easy use.

## Supported File Types :
- Images : ```.jpg, .jpeg, .png, .gif, .bmp```
- Documents : ```.pdf, .docx, .txt, .md```
- Archives : ```.zip, .rar, .7z, .tar, .gz```
- Executables : ```.exe, .msi, .bat, .sh```

## Installation :
Make sure Python is installed on your system. You can download Python from  - [python.org](https://www.python.org/downloads/).

## Requirements :
No additional libraries are needed. The script uses built-in Python modules : ```os, shutil, et sys```.

## Usage :
1. Download the script to your computer.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located using the ```cd``` command:

```cd path/to/the/script```
To run the script, provide the directory you want to organize as an argument. For example :

```python scriptName.py "C:/Users/User/Documents"```
Replace "C:/Users/User/Documents" with the actual path of the directory you want to organize.

Alternatively, if you're already in the directory where the script is located, you can just run:
```python scriptName.py```
- If you specify a directory path, the script will organize the files in that directory, moving them into corresponding subfolders like Images, Documents, Archives, etc.
- If no directory is specified, the script will use the current directory where the script is located and organize its files.

- The script will sort the files in the specified directory and create subfolders for each file type (e.g., "Images," "Documents," etc.).
- Files will be moved into their corresponding subfolders based on their extensions.

## Example Output :
If you run the script on a directory containing images, documents, and archives, you might see output like this :
```image1.jpg -> Images/```
```document1.pdf -> Documents/```
```archive1.zip -> Archives/```
Files will be moved into their respective subfolders (e.g., Images, Documents, Archives).

## Notes :
- The script ignores itself, so it will not move the script file into a subfolder.
- README files (or any file containing "README" in their name) will be ignored during the sorting process.
- If the specified directory does not exist, the script will display an error message.
- You can modify the supported file types in the ```CATEGORIES``` dictionary if needed.

## License :
This script is free to use and modify.
