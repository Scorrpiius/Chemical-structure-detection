import easyocr 
import numpy as np 
import cv2


chemical_dict = ["C", "N", "H", "O", "S", "-", "_", "=", "c", "n", "o", "s", "h", "]", "~", ";", ":", "z", "2", "0", "1", "3", "6", " ", "?", "}", "Na", "A", "Z"]

def to_be_removed(string: str) -> bool:

    """
    This function determines if the text can be removed or not.
    It checks if all the caracters in the string are in the chemical_dict 
    ( this dictionnary contains all the possible caracters that could be present
     in a chem structure )
    """

    length = len(string)
    chems = 0
    for c in chemical_dict:
        if string.count(c) > 0:
            chems = chems + len(c) * string.count(c)

    if chems == length:
        return False
    else: 
        return True
    

"""
The following functions always take the same arguments: 
    -- an input path, the path of the image to be analysed
    -- an output path, the path where the image will be saved

"""
def remove_text(input_path: str, output_path: str) -> None:

    """ 
    This function use the EASYOCR library to detect all the text in the image
    to then remove it. It removes only strings that are longer than 5 caracter
    ( using the hypothesis that no chemical related text is longer than 5 )
    """
    # Configuring the language for the ocr 
    reader = easyocr.Reader(['en']) 
    results = reader.readtext(input_path)

    # Read the image from the file path
    image = cv2.imread(input_path) 

    # Hide the text by adding a white polygon 
    for box in results: 

        x0, y0 = box[0][0] # Top left corner
        x1, y1 = box[0][1] # Top right corner
        x2, y2 = box[0][2] # Bottom right corner
        x3, y3 = box[0][3] # Bottom left corner


        x0, y0 = int(x0), int(y0)
        x1, y1 = int(x1), int(y1)
        x2, y2 = int(x2), int(y2)
        x3, y3 = int(x3), int(y3)

        points = np.array([[x0,y0],[x1,y1],[x2,y2],[x3,y3]])  
        
        if to_be_removed(box[1]) and len(box[1]) > 5 :
            cv2.fillPoly(image, pts=[points], color=(255,255,255))

    cv2.imwrite(output_path, image) # Save the image

def remove_lines(input_path: str, outputh_path: str) -> None:

    """
    This function removes the lines that could perturb the detection 
    of the chemical structures. The minimum length of lines detected
    is determined by the initial size of the picture (all the pictures
    are squared to make this easier)
    """
    
    image = cv2.imread(input_path)

    h,_,_ = image.shape

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    length = 50

    if h < 1000:
        length = 50
    elif h > 1000 and h < 2000:
        length = 70
    elif h > 2000 and h < 3000:
        length = 100
    elif h > 3000 and h < 4000:
        length = 135
    elif h > 4000:
        length = 140

    lines = cv2.HoughLinesP(edges, 1, np.pi/360, threshold=100 , minLineLength=length, maxLineGap=2 )

    for points in lines:
        x1,y1,x2,y2=points[0]
        cv2.line(image,(x1,y1),(x2,y2),(255,255,255),10)


    cv2.imwrite(outputh_path, image) #Save the image

def resize_image(input_path: str, outputh_path: str) -> None:

    """
    This function takes an image in input and modifies it 
    to make it a squared image
    """
    
    img = cv2.imread(input_path)

    #Getting the bigger side of the image
    s = max(img.shape[0:2])

    #Creating a dark square with NUMPY and making it white 
    f = np.ones((s,s,3),np.uint8)
    h = len(f)
    w = len(f[0])

    for y in range(h):
        for x in range(w):
            f[y,x] = [255,255,255]
        

    #Getting the centering position
    ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2

    #Pasting the 'image' in a centering position
    f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img

    #Showing results (just in case) 
    #cv2.imshow("IMG",f)
    #A pause, waiting for any press in keyboard
    #cv2.waitKey(0)

    #Saving the image
    cv2.imwrite(outputh_path,f)