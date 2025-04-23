################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Modellierung eines Generative Adversarial Networks (GAN): #


def GAN(length, initial_key, reference_key):

    k = 0

    while(True):

        sum = 0.0

        initial_key = CNOT(length, initial_key)

        if (k == 0): L = Generator(length, initial_key) 
        if (k > 0): L = Generator(length, M) 
        
        M = Diskriminator(length, L, reference_key)

        for j in range(0, length):

            sum = sum + M[j]

        k = k + 1

        if (sum == 0.0):

            return(initial_key)

            break
