import image
import ocr_tsrct
import parser
import mathpix

rnt = "/home/kronicmage/repos/api-examples/python/test.jpg"
theorem_statement = (200, 460, 1350, 600)
type_string = (850, 275, 1275, 360)
summation = (500, 775, 950, 1000)
all_of_them = [theorem_statement, type_string, summation]

def convert_to_latex(image_file_name, boundaries):
    # might want to sort boundaries? idk
    for_tesseract, for_mathpix = image.image_path_to_split_objects(image_file_name, boundaries)
    raw_mathpix_data = [mathpix.convert(x) for x in for_mathpix]
    raw_tesseract_data = ocr_tsrct.get_text_from_pil_object(for_tesseract)
    return raw_tesseract_data, raw_mathpix_data

def convert_object_to_latex(image_object, boundaries):
    for_tesseract, for_mathpix = image.separator(image_object, boundaries)
    raw_mathpix_data = [mathpix.convert(x) for x in for_mathpix]
    raw_tesseract_data = ocr_tsrct.get_text_from_pil_object(for_tesseract)
    print("% Raws: ", raw_mathpix_data, raw_tesseract_data)
    return raw_tesseract_data, raw_mathpix_data

## so convert_to_latex returns the raw output from the tesseract call,
## and a list of the raw outputs from mathpix calls for each bounding box

