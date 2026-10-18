def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3;
    match score:
        case _ if score >= 90:
            return "A"
        case _ if score >= 80:
            return "B"
        case _ if score >= 70:
            return "C"
        case _ if score >= 60:
            return "D"
        case _: 
            return "F"
​
    return score