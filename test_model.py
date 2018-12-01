from keras.models import load_model

classifier = load_model('Trained_model.h5')
#classifier.evaluate(steps = 1)

#Prediction of single image
def predictor():
    import numpy as np
    from keras.preprocessing import image
   # img_name = 'testimage'
    image_path = 'C:/Users/JALLURI KOUSHIK/Desktop/Simple-Sign-Language-Detector-master/testc.png'
    print('')
    
    test_image = image.load_img(image_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    #training_set.class_indices
    print('Predicted Sign is:')
    print('')
    if result[0][0] == 1:
         print("A")
         return 'A'
    elif result[0][1] == 1:
         print("B")
         return 'B'
    elif result[0][2] == 1:
         print("C")
         return 'C'
    elif result[0][3] == 1:
         print("D")
         return 'D'
    elif result[0][4] == 1:
         print("E")
         return 'E'
    elif result[0][5] == 1:
         print("F")
         return 'F'
    elif result[0][6] == 1:
         print("G")
         return 'G'
    elif result[0][7] == 1:
         print("H")
         return 'H'
    elif result[0][8] == 1:
         print("I")
         return 'I'
    elif result[0][9] == 1:
         print("J")
         return 'J'
    elif result[0][10] == 1:
         print("K")
         return 'K'
    elif result[0][11] == 1:
         print("L")
         return 'L'
    elif result[0][12] == 1:
         print("M")
         return 'M'
    elif result[0][13] == 1:
         print("N")
         return 'N'
    elif result[0][14] == 1:
         print("O")
         return 'O'
    elif result[0][15] == 1:
         print("P")
         return 'P'
    elif result[0][16] == 1:
         print("Q")
         return 'Q'
    elif result[0][17] == 1:
         print("R")
         return 'R'
    elif result[0][18] == 1:
         print("S")
         return 'S'
    elif result[0][19] == 1:
         print("T")
         return 'T'
    elif result[0][20] == 1:
         print("U")
         return 'U'
    elif result[0][21] == 1:
         print("V")
         return 'V'
    elif result[0][22] == 1:
         print("W")
         return 'W'
    elif result[0][23] == 1:
         print("X")
         return 'X'
    elif result[0][24] == 1:
         print("Y")
         return 'Y'
    elif result[0][25] == 1:
         print("Z")
         return 'Z'
         print("{} written!".format(img_name))
    img_text = predictor()
   print(img_text) 

