

# Find the index of second ,third duplicate element in string

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
sa        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

source = "ABABDBAAEDSBQEWBAFLSAFB"
#source = [12,23,3,4,12,56,78,12]
print(list_duplicates_of(source, 'B'))