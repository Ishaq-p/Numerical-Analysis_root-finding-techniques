
def rounding(num, fpa):
    fpa=int(fpa)
    num = float(num)
    num1 = num * 1e-10

    num2 = str(num1)
    fpa_points=[]
    exp=[]
    for ind, i in enumerate(num2):
        # print(i)
        if i=='e':
            exp.append(num2[ind:])
            break

        if i in ['1','2','3','4','5','6','7','8','9','0','.']:
            fpa_points.append(i)

    fpa_points_1 = str(round(float(''.join(fpa_points[0:fpa+2])), fpa-1))

    full_fpa = float(fpa_points_1 + ''.join(exp)) / 1e-10
    

    # fpa_points_2 = round(float(  ''.join(full_fpa)) / 1e-6)

    return num, num1, fpa_points, fpa_points_1, exp, full_fpa

# print(rounding(122.35, 4))