iterations = 652601
arrlen = 2

scores = [3, 7]

e1i = 0
e2i = 1

for i in range(iterations + 11):

    cur1 = scores[e1i]
    cur2 = scores[e2i]
    tot = cur1 + cur2

    if tot > 9:
        c1 = int(tot/10)
        c2 = tot % 10
        scores.append(c1)
        scores.append(c2)
        arrlen += 2
    else:
        arrlen += 1
        scores.append(tot)

    e1i += 1 + cur1
    e2i += 1 + cur2
    #print(scores, cur1, cur2, e1i, e2i, tot)

    e1i = e1i % arrlen
    e2i = e2i % arrlen
    #print(e1i, e2i, arrlen)

print("".join(str(i) for i in scores[iterations:iterations+10]))
    