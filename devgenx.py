import random

def generate_wells_month():
    
    res = {}
    total = random.randrange(11, 16) #10-15
    current = random.randrange(total-4, total)
    active = random.randrange(current-1, current)
    percent_found = ((active*100)/current)
    res['total'] = total
    res['current'] = current
    res['active'] = active
    res['percent_found'] = int(percent_found)
    
    return res


if __name__ == "__main__":
    x = generate_wells_month()
    print(type(x))
