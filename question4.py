from helper import *

# Question 4
# Write a script to extract all text and images from the provided PPTX and then translate all the
# text in file to English and then append the translated text under the original text back in
# slides, please try to keep the font size as reasonable as possible.    
def extractContentAndTranslate(file_path, output_folder="./output"):
    try:
        # check type of file
        check_file_type = checkFileType(file_path, ["pptx"])
        if check_file_type[0] is False:
            return 
        
        file_name = check_file_type[1]
        # read input file
        prs = Presentation(file_path)
        # get text file name
        text_file = checkOutputNameExisted(f"Q4_{file_name[0]}.txt", output_folder)
        # get image folder name
        image_folder = checkOutputNameExisted(f"Q4_{file_name[0]}_image", output_folder)
        os.makedirs(image_folder)
        text_out = open(text_file, "wb") 
        text_count = 1
        count = 1
        for slide in prs.slides:
            image_index = 1
            for shape in slide.shapes:
                if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                    image = shape.image
                    image_bytes = image.blob
                    # ---make up a name for the file, e.g. 'image.png'---
                    image_filename = f"{image_folder}/slide_{count}-image_{image_index}.png"
                    with open(image_filename, 'wb') as f:
                        f.write(image_bytes)
                    image_index += 1
                elif hasattr(shape, "text"):
                    new_text = f"\n{text_count}.\n" + f"- Original text:\n{shape.text}" + f"\n- Translated text:\n{GoogleTranslator(source='auto', target='en').translate(shape.text)}"
                    text_out.write(new_text.encode("utf8"))
                    text_count += 1
                    
            count += 1
        text_out.close()     
        
    except Exception as err:
        print("Opp! File processing failed")
        print(err)

extractContentAndTranslate("./input/Networking.pptx")