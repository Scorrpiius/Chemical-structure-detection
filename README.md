# Chemical-structure-detection

# How to install the libraries needed
The code uses DECIMER-Segmentation and DECIMER, two powerful tools that can isolate chemical structures in a document, and get the SMILES formula of each structure detected. 
```
$ pip install easyocr
$ pip install opencv-python
$ pip install numpy
$ pip install aspose-words
$ pip install torchvision
$ pip install Pillow

$ pip install DECIMER
$ git clone https://github.com/Kohulan/DECIMER-Image-Segmentation
$ cd DECIMER-Image-Segmentation
$ pip install .
```
- You also need to [download poppler](https://poppler.freedesktop.org/) for the DECIMER-Image-Segmentation tool. 
- You have to manually change the path to the poppler on the code. To change it got to the file "document_processing.py" and change it on line 54 (see the code for a path example)

## Note
- There is a slight change to do in the DECIMER-Image-Segmentation code for it to work properly.
- On your computer got to "DECIMER-Image-Segmentation\decimer_segmentation\decimer_segmentation.py" and on line 365 change the Image.ANITALIAS with Image.Resampling.LANCZOS

# How to use the code

```
$ git clone https://github.com/Scorrpiius/Chemical-structure-detection.git
$ cd Chemical-structure-detection
$ python3 chemical_detection.py folder_path (this folder should contain all the images you want to analyse)
```
## Example 
The images you want analysed are in "C:\User\Document\Images". To execute the code you have to run :
```
$ python3 chemical_detection.py "C:\User\Document\Images"
```

# Citations
- For DECIMER-Segmentation: Rajan, K., Brinkhaus, H.O., Sorokina, M. et al. DECIMER-Segmentation: Automated extraction of chemical structure depictions from scientific literature. J Cheminform 13, 20 (2021). https://doi.org/10.1186/s13321-021-00496-1
- For DECIMER : Rajan K, Brinkhaus HO, Agea MI, Zielesny A, Steinbeck C (2023) DECIMER.ai - An open platform for automated optical chemical structure identification, segmentation and recognition in scientific publications. ChemRxiv. doi: https://10.26434/chemrxiv-2023-xhcx9
Rajan, K., Zielesny, A. & Steinbeck, C. DECIMER 1.0: deep learning for chemical image recognition using transformers. J Cheminform 13, 61 (2021). https://doi.org/10.1186/s13321-021-00538-8
