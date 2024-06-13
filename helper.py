import pymupdf
import os
from deep_translator import GoogleTranslator
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

def checkFileType(file_path, file_types):
    file_paths = file_path.split('/')
    file_fullname = file_paths[-1]
    file_name = file_fullname.split('.')
    
    # check invalid file name
    if len(file_name) == 0 or file_name[-1] not in file_types:
        print("This type of file is not supported")
        return (False)
    
    return (True, file_name)   

# check whether file/folder existed
def checkOutputNameExisted(output_name, output_folder="./output"):
    count = 1
    file_name = f"{output_folder}/{output_name}"
    name_checker = os.path.exists(file_name)
    
    # if name existed, appending a version number to file/folder name
    while name_checker is True:
        file_name = f"{output_folder}/[{count}]{output_name}"
        name_checker = os.path.exists(file_name) 
        count += 1

    return file_name

def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2 ** 0:
        l.append("superscript")
    if flags & 2 ** 1:
        l.append("italic")
    if flags & 2 ** 2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2 ** 3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2 ** 4:
        l.append("bold")
    return ", ".join(l)
    