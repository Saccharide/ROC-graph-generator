##################################################################################################
'''
// @Project      ROC Graph Generator (Receiver Operating Characteristic)
// @Author       Saccharide
'''
##################################################################################################

import matplotlib.pyplot as plt
import numpy as np



def graph(attack_packets, benign_packets):

    # Getting the maximum size T
    maxAttackSize  = max(attack_packets)
    maxBenignSize  = max(benign_packets)
    maxIterateSize = max([maxAttackSize, maxBenignSize])

    # Setting up the x (false positives) and y (true positives) to plot
    false_positives_list = []
    true_positives_list  = []

    # Iterate from t = 0 to T, and calculate the corresponding TPR and FPR
    for t in range(maxIterateSize+1):

        # Finding the True Positives
        true_positive = [ x for x in attack_packets if x <= t]
        true_positive_rate = float(len(true_positive)) / len(attack_packets)

        # Finding the False Positives
        false_positive = [ x for x in benign_packets if x <= t] 
        false_positive_rate = float(len(false_positive)) / len(benign_packets)

        # Adding them to their respective lists
        true_positives_list.append(true_positive_rate)
        false_positives_list.append(false_positive_rate)


        # Printing for debugging:
        # print("Current iteration t = ",t)        
        print("# of True Positive  = ", len(true_positive))
        print("True Positive Rate  = ", true_positive_rate)
        print("")
        print("# of False Positive = ", len(false_positive))
        print("False Positive Rate = ", false_positive_rate)
        print("-------------------------------------------") 


    print("True Positive list = ", true_positives_list)
    print("False Postive list = ", false_positives_list)
    # Graph them with matplotlib
    plt.scatter(false_positives_list, true_positives_list, clip_on=False)
    plt.plot(false_positives_list, true_positives_list, clip_on=False)
    
    # Adding label to the graph
    plt.suptitle('ROC Graph')
    plt.xlabel('False Positive Rate', fontsize = 18)
    plt.ylabel('True Positive Rate' , fontsize = 18)
    
    # Sets up the x and y limits
    axes = plt.gca()
    axes.set_ylim([0.0,1.0])
    axes.set_xlim([0.0,1.0])

    plt.show()

attack_packets = [1,2,2,3,3,6,6,10]
benign_packets = [3,3,5,6,7,7,8,8,8,9]

graph(attack_packets, benign_packets)
