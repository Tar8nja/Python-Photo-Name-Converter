# Python-Photo-Name-Converter
Changes the name to the date of the creation of each file. Modifications of the file will not interfere with the name given by the code. Works with [images and video](#files-supported).

The only dependency is Python3. I haven't checked other versions of Python, but getting around and making a version that suits you shouldn't be a big problem for a smart fella like you.
I hope this works well, it does for me.

## Files Supported

*  .jpg
*  .jpeg
*  .png
*  .raw
*  .arw
*  .mp4
*  .mts
*  .nef

## Important information

1.  Accesses the data of the file, extracts the creation date and uses it as the new file name.
2.  Mantains the UPPER/lower case of the file extension.
3.  Converts '.mts' to '.mp4'.
4.  To add file extensions, moddify the list 'SUPPORTED_FILE_EXTENSIONS'.
5.  I can only guarantee that the code is safe for the current file types. Adding any by yourself is on your behalf.  

## Instructions of use

1.  Download the '.py' file from this repo.
2.  Place the '.py' file at the same directory (same folder) as the media.
3.  Execute the '.py' file.
4.  Follow the instructions given by the program.
