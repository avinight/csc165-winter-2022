def get_165() -> float:
    """Return your final mark for CSC165."""
    preps = 100  # prep quizzes and TT0/PS0
    ps1 = float(input("What was your grade on PS1 (%)?"))
    ps2 = float(input("What was your grade on PS2 (%)?"))
    ps3 = float(input("What is your projected Third Problem Set mark (%)?"))
    ps4 = float(input("What is your projected Final Problem Set mark? (%)"))
    tt1 = float(input("What was your grade on Term Test 1 (%)?"))
    tt2 = float(input("What is your projected Term Test 2 mark?"))
    final = float(input("What is your projected exam mark?"))
    all_p = [ps1, ps2, ps3, ps4]
    all_p.sort()
    worst_p = all_p[0]
    mid1_p = all_p[1]
    mid2_p = all_p[2]
    best_p = all_p[3]

    return preps*0.03 + best_p*0.08 + worst_p*0.06 + mid1_p*0.07 \
           + mid2_p*0.07 + tt1*0.17 + tt2*0.17 + final*0.34
