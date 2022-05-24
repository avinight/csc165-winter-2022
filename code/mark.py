def get_165() -> float:
    """Return your final mark for CSC165."""
    preps = 100  # prep quizzes and TT0/PS0
    ps0 = float(75)
    ps1 = float(97.22)
    ps2 = float(98.39)
    ps3 = float(99.22)
    ps4 = float(98.28)
    tt1 = float(76.72)
    # tt1 = float(90)
    tt2 = float(90.56)
    final = float(80)
    all_p = [ps1, ps2, ps3, ps4]
    all_p.sort()
    worst_p = all_p[0]
    mid1_p = all_p[1]
    mid2_p = all_p[2]
    best_p = all_p[3]

    return ps0*0.01 + preps*0.03 + best_p*0.08 + worst_p*0.06 + mid1_p*0.07 \
           + mid2_p*0.07 + tt1*0.17 + tt2*0.17 + final*0.34


def get_148() -> float:
    preps = float(88.61)
    labs = float(88.89)
    survey = 100
    a0 = float(96.38)
    a1 = float(99.11)
    a2 = float(97.4)
    midterm = float(95.71)
    # final = 90
    final = float(94.74)

    return preps*0.1 + labs*0.09 + survey*0.01 + a0*0.05 + a1*0.13 + a2*0.13 + \
           midterm*0.15 + final*0.34
