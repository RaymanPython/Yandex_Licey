import sys
'''
var
n, count, sum_time, max_process, i: integer;
start_time, end_time, start_process, end_process: int64;
time_process: array[1..604800] of
integer;
f: text;
begin
assign(f, 'C:\26.txt');
reset(f);
readln(f, n);
'''
time_process = [0 for i in range(6048001)]
start_time = 1633305600
end_time = start_time + 604800
count = 0
sys.stdin = open('unix.txt', 'r')
n = int(int(input()))
for line in sys.stdin:
    s = line.rstrip('\n')[::-1]
    if s == '':
        break
    start_process, end_process = map(int, s.split())
    if (start_process < start_time) and ((end_process > start_time) or (end_process == 0)):
        count += 1
    if (start_process >= start_time) and (start_process <= end_time):
        time_process[start_process - start_time] = time_process[start_process - start_time] + 1
    if (end_process >= start_time) and (end_process <= end_time):
        time_process[end_process - start_time] -= 1
sum_time = 0
max_process = 0
for i in range(1, 604802):
    count += time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time += 1
print(max_process, sum_time)
