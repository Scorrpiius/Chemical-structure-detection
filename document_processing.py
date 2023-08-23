import os
import aspose.words as aw
import DECIMER as dc
import decimer_segmentation as ds
from image_processing import resize_image, remove_lines, remove_text
import matplotlib.pyplot as plt
import mplcursors


            
def document_processing(directorypath: str, visualisation: bool = True):
    text_removed_path = directorypath + "\\Text removed"
    lines_removes_path = directorypath + "\\Lines removed"
    resized_images_path = directorypath + "\\Resized images"
    pdf_files_path = directorypath + "\\PDF files"
    segments_path = directorypath + "\\Segmented PDFs"

    folders_list = [text_removed_path, lines_removes_path, resized_images_path, pdf_files_path, segments_path]
    
    os.mkdir(text_removed_path)
    os.mkdir(lines_removes_path)
    os.mkdir(resized_images_path)
    os.mkdir(pdf_files_path)
    os.mkdir(segments_path)

    print("Removing the texts from the images........")
    for file in os.listdir(directorypath):
        filepath = directorypath + "\\" + file
        if filepath not in folders_list:
            remove_text(directorypath + "\\" + file, text_removed_path + "\\" +  file)

    print("Resizing the images........")
    for file in os.listdir(text_removed_path):
        filepath = text_removed_path + "\\" + file
        if filepath not in folders_list:
            resize_image(text_removed_path + "\\" + file, resized_images_path + "\\" +  file)


    print("Removing the lines from the images........")
    for file in os.listdir(resized_images_path):
        filepath = resized_images_path + "\\" + file
        if filepath not in folders_list:
            remove_lines(resized_images_path + "\\" + file, lines_removes_path + "\\" +  file)

    print("Saving the images as PDF files........")
    for file in os.listdir(lines_removes_path):
        filepath = lines_removes_path + "\\" + file
        if filepath not in folders_list:
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc)
            builder.insert_image(filepath)
            doc.save(pdf_files_path + "\\" + file[:-4] + ".pdf")

    print("Segmenting PDF files........")
    segmented_pdf_list = []
    for file in os.listdir(pdf_files_path):
        filepath = pdf_files_path + "\\" + file
        raw_segments = ds.segment_chemical_structures_from_file(filepath, expand=True, poppler_path="C:\\Program Files (x86)\\poppler-23.07.0\\Library\\bin")
        segmented_pdf = segments_path + "\\" + file[:-4]
        normalized_segments = [ds.get_square_image(segment, 350) for segment in raw_segments]
        ds.save_images(normalized_segments, 
                    segmented_pdf, 
                    f"{os.path.split(filepath)[1][:-4]}_norm",
        )
        segmented_pdf_list.append(segmented_pdf)
        print(f"Segments saved at {segmented_pdf}.")

    
    print("Analysing segments........")
    smiles_formulas = []
    for path in os.listdir(segments_path):
        txt_filepath = segments_path + "\\" + path + ".txt"
        smiles_txt = open(txt_filepath, "w+")


        for file in os.listdir(segments_path + "\\" + path):
            smiles_formula = dc.predict_SMILES(segments_path + "\\" + path + "\\" + file)
            lists = smiles_formula.split('.')
            smiles_txt.write("The analysed image:" + file + " and the SMILES formula:" + smiles_formula + "\n")
            for element in lists:
                #print(element)
                if len(element) > 6:
                    smiles_formulas.append(element)

    if visualisation == True:
        dict = {}
        for formula in smiles_formulas:
            dict[formula] = smiles_formulas.count(formula)
            
        sorted_values = sorted(dict.values()) # Sort the values
        sorted_dict = {}

        for i in sorted_values:
            for k in dict.keys():
                if dict[k] == i:
                    sorted_dict[k] = dict[k]


        plt.barh(list(sorted_dict.keys()), sorted_dict.values(), color='g', align='edge')
        plt.yticks(fontsize=4)
        mplcursors.cursor(hover=True)
        plt.show()
        

