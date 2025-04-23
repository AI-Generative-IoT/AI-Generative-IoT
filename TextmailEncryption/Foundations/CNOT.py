################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Modellierung eines GAN Diskriminators #

def CNOT(length, input_key): # Defines a pairwise CNOT-Operation

    output_key = [0.0]*length
    
    output_key[1] = 1.0
    output_key[2] = 1.0
        
    for k in range(0, M):

        if (input_key[k] == 1 and input_key[k-1] == 0): input_key[k-1] = 1        
        if (input_key[k] == 1 and input_key[k-1] == 1): input_key[k-1] = 0        

        output_key[k] = input_key[k]
        output_key[k-1] = input_key[k-1]

    return output_key
