# -*- coding: utf-8 -*-

from copy import deepcopy

g_water = [8, 0, 0]

buckets = (8, 5, 3)

result_right = (4, 4, 0)

records = set()

def getAction(water, records):

    for i in range(3):
        for j in range(3):

            #print i, j
            water_l = pour(i, j, water)
            if not water_l:
                continue

            if water_l and water_l == result_right:
                records.add(water_l)
                break

            else:
                print records
                if water_l not in records:
                    records.add(water_l)
                    getAction(water_l, records)


#倒水动作

def pour(bucket_from, bucket_to, water):
    water = deepcopy(water)

    if water[bucket_from] > 0 and water[bucket_to] < buckets[bucket_to]:
        quantity = 0
        if buckets[bucket_to] - water[bucket_to] >= water[bucket_from]:
            quantity = water[bucket_from]
        else:
            quantity = buckets[bucket_to] - water[bucket_to]


        flag = [water[0], water[1], water[2]]



        flag[bucket_from] = flag[bucket_from] - quantity
        flag[bucket_to] = flag[bucket_to] + quantity

        return (flag[0], flag[1], flag[2])




if __name__ == '__main__':
    '''
    print water[0]

    print pour(0, 1, 2)

    print pour(1, 2, 2)

    print pour(1, 0, 2)
    print pour(2, 1, 2)
    print pour(0, 2, 2)
    '''
    getAction(g_water, records)

