from helper import *

# Question 2
# For each paragraph in the PDF/DOCX, extract the following details: Text content, Font type, Font size, Styling elements, Text color
def extractTextDetail(file_path, output_folder="./output"):
    try:
        # check type of file
        check_file_type = checkFileType(file_path, ["pdf", "docx"])
        if check_file_type[0] is False:
            return 
        
        file_name = check_file_type[1]
        # read input file
        doc = pymupdf.open(file_path)
        # get text file name
        text_file = checkOutputNameExisted(f"Q2_{file_name[0]}.txt", output_folder)
        count = 1   
        page_count = 1
        extract_dict = {}
        text_out = open(text_file, "wb") 
        page_blocks = {}
        # visit every page of input file
        for page in doc:
            blocks = page.get_text("dict", flags=11)["blocks"]
            extract_dict = {}
            for block in blocks:
                temp_dict_detail = {}
                for line in block["lines"]:  # iterate through the text lines
                    for span in line["spans"]:  # iterate through the text spans
                        if len(temp_dict_detail.keys()) == 0: 
                            temp_dict_detail["text"] = span["text"]
                            temp_dict_detail["font"] = span["font"]
                            temp_dict_detail["size"] = span["size"]
                            temp_dict_detail["style"] = flags_decomposer(span["flags"])
                            temp_dict_detail["color"] = span["color"]
                        else:
                            if temp_dict_detail["font"] == span["font"] and temp_dict_detail["size"] == span["size"] and temp_dict_detail["style"] == flags_decomposer(span["flags"]) and temp_dict_detail["color"] == span["color"]:
                                temp_dict_detail["text"] += span["text"]
                            else:
                                temp_dict_detail["color"] = "#%06x"%(temp_dict_detail["color"])
                                result = f"\n{count}\nText: {temp_dict_detail['text']}\nFont type: {temp_dict_detail['font']}\nFont size: {temp_dict_detail['size']}\nStyle: {temp_dict_detail['style']}\nText color: {temp_dict_detail['color']}"
                                if block["number"] in list(extract_dict.keys()):
                                    extract_dict[block["number"]] += [temp_dict_detail]
                                else:
                                    extract_dict[block["number"]] = [temp_dict_detail]
                                text_out.write(result.encode("utf8"))
                                temp_dict_detail = {}
                                temp_dict_detail['text'] = span["text"]
                                temp_dict_detail['font'] = span["font"]
                                temp_dict_detail['size'] = span["size"]
                                temp_dict_detail['style'] = flags_decomposer(span["flags"])
                                temp_dict_detail['color'] = span["color"]
                                count += 1
                            
                if len(temp_dict_detail) != 0: 
                    temp_dict_detail["color"] = "#%06x"%(temp_dict_detail["color"])
                    result = f"\n{count}\nText: {temp_dict_detail['text']}\nFont type: {temp_dict_detail['font']}\nFont size: {temp_dict_detail['size']}\nStyle: {temp_dict_detail['style']}\nText color: {temp_dict_detail['color']}"
                    if block["number"] in list(extract_dict.keys()):
                        extract_dict[block["number"]] += [temp_dict_detail]
                    else:
                        extract_dict[block["number"]] = [temp_dict_detail]
                    text_out.write(result.encode("utf8"))
                    count += 1
                    
            page_blocks[page_count] =  extract_dict
            page_count += 1
        text_out.close()   
        convertTextToUpperCase(page_blocks, file_name, output_folder)
        
    except Exception as err:
        print("Opp! File processing failed")
        print(err)

# Question 3
# Convert the text of each extracted paragraph to UPPERCASE. Subsequently, compile all the
# UPPERCASE paragraphs into a new PDF/DOCX, maintaining the original formatting (font type
# and styling) as closely as possible.        
def convertTextToUpperCase(extracted_paragraphs, file_name, output_folder):
    text_file = checkOutputNameExisted(f"Q3_{file_name[0]}.pdf", output_folder)
    doc = pymupdf.open()  # new or existing PDF
    for blocks in extracted_paragraphs.values():
        paragraphs_content = "<p>" 
        page = doc.new_page()  # new or existing page via doc[n]
        for paragraphs in blocks.values():
            for paragraph in paragraphs:
                paragraph_content = f"""
                    <span style="font-family: {paragraph['font']}, {paragraph['style']}; color: {paragraph['color']}; font-size: {round(paragraph['size'])}px;">{paragraph['text'].upper()}</span>
                """
                if "bold" in paragraph["style"]:
                    paragraph_content = f"<b>{paragraph_content}</b>"
                if "italic" in paragraph["style"]:
                    paragraph_content = f"<i>{paragraph_content}</i>"
                paragraphs_content += paragraph_content
            paragraphs_content += "</p>"
        page.insert_htmlbox(page.rect, paragraphs_content)   
    
    doc.save(text_file)
    
extractTextDetail("./input/pdf_mock_file.pdf")
extractTextDetail("./input/docx_mock_file.docx")