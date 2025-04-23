################################################################################################################################################
#                                                                                                                                              #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt    #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Modellierung eines GAN Diskriminators #

def Diskriminator(length, input_key, ideal_key):

    difference = [0.0]*(length + 1)

    for j in range(0, length):

        difference[j] = math.fabs(ideal_key[j] - input_key[j])

    return(difference)
