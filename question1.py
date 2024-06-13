from helper import *

# Question 1
# Write a script to extract all text and images from the provided PDF/DOCX. Ensure that all images are saved to the disk.
def extractFileContent(file_path, output_folder="./output"):
    try:
        # check type of file
        check_file_type = checkFileType(file_path, ["pdf", "docx"])
        if check_file_type[0] is False:
            return 
        
        file_name = check_file_type[1]
        # read input file
        doc = pymupdf.open(file_path)
        # get text file name
        text_file = checkOutputNameExisted(f"Q1_{file_name[0]}.txt", output_folder)
        # get image folder name
        image_folder = checkOutputNameExisted(f"Q1_{file_name[0]}_image", output_folder)
        count = 1   
        os.makedirs(image_folder)
        text_out = open(text_file, "wb") 

        # visit every page of input file
        for page in doc:
            text = page.get_text().encode("utf8")
            text_out.write(text)
            image_list = page.get_images()
            
            for image_index, img in enumerate(image_list, start=1): # enumerate the image list
                xref = img[0] # get the XREF of the image
                pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

                if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

                pix.save(f"{image_folder}/page_{count}-image_{image_index}.png") # save the image as png
                pix = None
            count += 1
            
        text_out.close()     
        
    except Exception as err:
        print("Opp! File processing failed")
        print(err)
        
extractFileContent("./input/pdf_mock_file.pdf")
extractFileContent("./input/docx_mock_file.docx")