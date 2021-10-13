data = open('input.txt', 'r').read().split('\n')

def find_smallest_side(x, y, z):
    if x*z < x*y:
        if x*z < z*y:
            return x*z
        else:
            return z*y
    else:
        if x*y < z*y:
            return x*y
        else:
            return z*y


def find_perimeter(x, y, z):
    sides = [x,y,z]
    sides.sort()
    ribbon_wrap = (2*sides[0]) + (2*sides[1])
    ribbon_bow = sides[0]*sides[1]*sides[2]
    return ribbon_bow+ribbon_wrap

paper_needed = 0
ribbon_needed = 0

for i in data:
    if len(i) > 1:

        pres_dim = i.split('x')

        for j in range(len(pres_dim)):
            pres_dim[j] = int(pres_dim[j])

        pres_area = (2*pres_dim[0]*pres_dim[1]) + (2*pres_dim[1]*pres_dim[2]) + (2*pres_dim[2]*pres_dim[0])

        extra = find_smallest_side(pres_dim[0],pres_dim[1],pres_dim[2])
        ribbon_for_pres = find_perimeter(pres_dim[0],pres_dim[1],pres_dim[2])
        paper_needed = paper_needed + extra + pres_area
        ribbon_needed += ribbon_for_pres
        print('PRES DIM', pres_dim)
        print('area', pres_area)
        print('extra', extra)

print('the paper needed is:', paper_needed, 'sqft')
print('the ribbon needed is:', ribbon_needed, 'sqft')