# Chemical-structure-detection
# Pré requis
Il faut les dernières versions de python et pip

# Installer les librairies nécessaires
```
$ pip install -r requirements.txt

$ git clone https://github.com/Kohulan/DECIMER-Image-Segmentation
$ cd DECIMER-Image-Segmentation
$ pip install .
```
- Il faut également installer un logiciel Poppler (https://poppler.freedesktop.org/) et changer le chemin d'accès vers ce logiciel dans le code. Pour le changer il faut aller sur le fichier "document_processing.py" et changer le chemin d'accès à la ligne 54.
## Note
- Il y aussi un changement à faire dans le code de DECIMER-Image-Segmentation pour qu'il marche correctement. Dans le dossier où vous avez executez la commande "git clone https://github.com/Kohulan/DECIMER-Image-Segmentation" vous trouverez le dossier DECIMER-Image-Segmentation. Il faut suivre le chemin suivant: "DECIMER-Image-Segmentation\decimer_segmentation" et dans le fichier "decimer_segmentation.py" il faut changer 'Image.ANITALIAS' avec 'Image.Resampling.LANCZOS' à la ligne 365

# Installer et utiliser le code

```
$ git clone https://github.com/Scorrpiius/Chemical-structure-detection.git
$ cd Chemical-structure-detection
$ python3 chemical_detection.py chemin_dossier (c'est le chemin d'accès du dossier où les images que vous voulez analyser se trouvent)
```

## Exemple 
Les images à analyser sont dans le dossier "C:\User\Document\Images". Il faut alors executer la commande suivante:
```
$ python3 chemical_detection.py "C:\User\Document\Images"
```
## Options
On peut choisir de visualiser les résultats sous la forme d'un histogramme , il faut simplement rajouter une option dans la commande initiale:
```
$ python3 chemical_detection.py "C:\User\Document\Images" True
```
- Par défaut quand il n'y a qu'un seul paramètre, l'histogramme s'affiche
- Pour ne pas visualiser l'histogramme il faut mettre False en option
- 
# Erreur courante
Si jamais il y a des erreurs de type "No module named ..." c'est qu'il faut sûrement installer la librairie en question. Cela se fait avec la commande pip:
```
 $ pip install module_name (module_name étant le nom de la librairie manquante)
 ```
# Composition
- Le dossier Samples contient des exemples de schémas de dégradation pour tester le code.
- Le fichier image_processing.py contient des fonctions qui modifient les images pour optimiser la reconnaissance des structures chimiques par DECIMER-Image-Segmentation.
- Le fichier document_processing.py s'occupe d'éxecuter les fonctions d'image_processing.py sur les images et ensuite, fait appel à DECIMER-Image-Segmentation pour isoler les structures chimiques de chaque image, puis à DECIMER pour extraire la formule SMILES de chaque image de molécule.
- Le fichier requirements.txt contient toutes les libraires à installer.
  
# Pre requisite
You need the latest versions of python and pip
# How to install the libraries needed
```
$ pip install -r requirements.txt

$ git clone https://github.com/Kohulan/DECIMER-Image-Segmentation
$ cd DECIMER-Image-Segmentation
$ pip install .
```
- You also need to [download poppler](https://poppler.freedesktop.org/) for the DECIMER-Image-Segmentation tool. 
- You have to manually change the path to the poppler on the code. To change it go to the file "document_processing.py" and change it on line 54 (see the code for a path example)

## Note
- There is a slight change to do in the DECIMER-Image-Segmentation code for it to work properly.
- On your computer go to "DECIMER-Image-Segmentation\decimer_segmentation\decimer_segmentation.py" and on line 365 change the Image.ANITALIAS with Image.Resampling.LANCZOS

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

## Options
You can choose to visualize the results in a histogram. To do so, run the following command:
```
$ python3 chemical_detection.py "C:\User\Document\Images" True
```
- By default, with only one parameter, the visualisation is set to True
- To not see the histogram, you have to write False
- 
# Common error
Sometimes, not all the modules needed are installed, and you get a "No module named ..." error. You can fix this by running this command: 
```
 $ pip install module_name (module_name being the missing module)
 ```
# Repository layout
- The Samples folder contains exemples of degradation patterns to test the code.
- The file image_processing.py contains functions that modifies the images to optimize the chemical structure recognition by the DECIMER-Image-Segmentation tool.
- The file document_processing.py executes the previous functions on every image, call the DECIMER-Image-Segmentation tool to isolates the chemical structures then call DECIMER to get the SMILES formula of each segmented image.
- The file requirements.txt contains all the necessary libraries for the code to execute well.

# Citations
- For DECIMER-Segmentation: Rajan, K., Brinkhaus, H.O., Sorokina, M. et al. DECIMER-Segmentation: Automated extraction of chemical structure depictions from scientific literature. J Cheminform 13, 20 (2021). https://doi.org/10.1186/s13321-021-00496-1
- For DECIMER : Rajan K, Brinkhaus HO, Agea MI, Zielesny A, Steinbeck C (2023) DECIMER.ai - An open platform for automated optical chemical structure identification, segmentation and recognition in scientific publications. ChemRxiv. doi: https://10.26434/chemrxiv-2023-xhcx9
Rajan, K., Zielesny, A. & Steinbeck, C. DECIMER 1.0: deep learning for chemical image recognition using transformers. J Cheminform 13, 61 (2021). https://doi.org/10.1186/s13321-021-00538-8
