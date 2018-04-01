
import matplotlib.pyplot as plt
import numpy as np



def graph(attack_packets, benign_packets):

    
    maxAttackSize = max(attack_packets)
    maxBenignSize  = max(benign_packets)

    maxIterateSize = max([maxAttackSize, maxBenignSize])


    for t in range(maxIterateSize+1):
        true_positive = [ x for x in attack_packets if x <= t]

        true_positive_rate = float(len(true_positive)) / len(attack_packets)

        false_positive = [ x for x in benign_packets if x <= t] 

        false_positive_rate = float(len(false_positive)) / len(benign_packets)

        print("True Positive Rate = ", true_positive_rate)
        
        print("False Positive Rate = ", false_positive_rate)

attack_packets = [1,1,2,3,5,8]
benign_packets = [2,2,4,6,6,7,8,9]

graph(attack_packets, benign_packets)
