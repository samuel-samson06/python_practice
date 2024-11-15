from datetime import datetime
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    t1_converted = datetime.strptime(t1,format)
    t2_converted = datetime.strptime(t2,format)
    difference = abs(t2_converted-t1_converted)
    return int(difference.total_seconds())
if __name__ == '__main__':
    t = int(input("Run::"))
    for t_itr in range(t):
        t1 = input("Date 1::")
        t2 = input("Date 2::")
        delta = time_delta(t1, t2)
        print(delta)