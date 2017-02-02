# py-unoconv-batch-recursive

Working but not clean python script for converting files to PDF recursively

### Synopsis ###
This is my very first Python script, but it is working. You can batch convert files with `unoconv` to PDF format.

### Requirements ###
You need the following to be installed:
- Python
- Libre Office
- unoconv

### How it works ###

When you start this programm with:

    python py-unoconv-batch-recursive

without any parameters it will use the folder where it resides as the base folder for the conversion

You can however use:

    python /path/to/script/py-unoconv-batch-resursive --in="/path/to/documents"
    
### Default extensions ###
doc,docx,rtf,txt,otf

You can change this by adding:

    -ext="doc docx"
    
Now it will only select these extensions

### Generated filenames ###
The filenames generated are when the file converted is `somefile.docx`, will become `somefile.docx.pdf`.
This is to avoid that a filename with `doc` and `docx` with the same basename in a folder will be overwritten.

      
