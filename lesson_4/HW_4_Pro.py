with open('log1', mode='r') as f:
    data = f.read()

#print(data)
data = data.split('\n')


from datetime import datetime

line = data[0][:19]
last_log = datetime.strptime(line, '%Y-%m-%d %H:%M:%S')
for line in data:
    log_time = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
    if last_log < log_time: last_log = log_time

print(last_log)