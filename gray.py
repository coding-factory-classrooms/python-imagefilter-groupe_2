import cv2
import os
import logger



def gray_pic(dossierE, dossierS):
    """
        applies a black & white filter on all images of the directory 'imgs', catching errors (such as wrong name, or wrong type of file) if encountered
        :param dossierE: the directory from which we get the image to modify
        :param dossierS: the directory where the modified image is saved

        """
    files = os.listdir(dossierE)
    for f in files:
        if f.endswith('.jpg'):
            print("1er if (pour .jpg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f"{dossierS}/{f}", gray)
                logger.log(f'gray_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        elif f.endswith('.jpeg'):
            print("elif (pour .jpeg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f"{dossierS}/{f}", gray)
                logger.log(f'gray_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        elif f.endswith('.png'):
            print("2ème elif (pour .png)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(f"{dossierS}/{f}", gray)
                logger.log(f'gray_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        else:
            print("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            logger.log("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            print(f)













