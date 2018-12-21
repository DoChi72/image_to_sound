#Cmajor
def Cmajor(cltCenters_list, n_clusters, assignmentFreq):
    n = 0
    for x in range(n_clusters):
        m = 0
        if 0 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 31:
            assignmentFreq[n][m] = 261.63
        elif 31 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 63:
            assignmentFreq[n][m] = 293.66
        elif 63 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 95:
            assignmentFreq[n][m] = 329.63
        elif 95 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 127:
            assignmentFreq[n][m] = 349.23
        elif 127 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 159:
            assignmentFreq[n][m] = 392.00
        elif 159 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 191:
            assignmentFreq[n][m] = 440.00
        elif 191 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 223:
            assignmentFreq[n][m] = 493.88
        elif 223 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 255:
            assignmentFreq[n][m] = 523.25
        m = m+1
        for y in range(2):
            if 0 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 31:
                assignmentFreq[n][m] = 261.63
            elif 31 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 63:
                assignmentFreq[n][m] = 293.66
            elif 63 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 95:
                assignmentFreq[n][m] = 329.63
            elif 95 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 127:
                assignmentFreq[n][m] = 349.23
            elif 127 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 159:
                assignmentFreq[n][m] = 392.00
            elif 159 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 191:
                assignmentFreq[n][m] = 440.00
            elif 191 <= cltCenters_list[n][m] and cltCenters_list[n][m] < 223:
                assignmentFreq[n][m] = 493.88
            elif 223 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 255:
                assignmentFreq[n][m] = 523.25
            m = m+1
        n = n+1
    print(assignmentFreq)
    return assignmentFreq

#
def Aminor(cltCenters_list, n_clusters, assignmentFreq):
    n = 0
    for x in range(n_clusters):
        m = 0
        if 0 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 31:
            assignmentFreq[n][m] = 220.00
        elif 32 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 63:
            assignmentFreq[n][m] = 246.94
        elif 64 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 95:
            assignmentFreq[n][m] = 261.63
        elif 96 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 127:
            assignmentFreq[n][m] = 293.66
        elif 128 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 159:
            assignmentFreq[n][m] = 329.63
        elif 160 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 191:
            assignmentFreq[n][m] = 349.23
        elif 192 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 223:
            assignmentFreq[n][m] = 415.30
        elif 224 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 255:
            assignmentFreq[n][m] = 440.00
        m = m+1
        for y in range(2):
            if 0 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 31:
                assignmentFreq[n][m] = 220.00
            elif 32 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 63:
                assignmentFreq[n][m] = 246.94
            elif 64 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 95:
                assignmentFreq[n][m] = 261.63
            elif 96 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 127:
                assignmentFreq[n][m] = 293.66
            elif 128 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 159:
                assignmentFreq[n][m] = 329.63
            elif 160 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 191:
                assignmentFreq[n][m] = 349.23
            elif 192 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 223:
                assignmentFreq[n][m] = 415.30
            elif 224 <= cltCenters_list[n][m] and cltCenters_list[n][m] <= 255:
                assignmentFreq[n][m] = 440.00
            m = m+1
        n = n+1
    print(assignmentFreq)
    return assignmentFreq