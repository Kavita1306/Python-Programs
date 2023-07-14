from datetime import datetime
start_time="5:52:20"
end_time="9:45:37"
t1=datetime.strptime(start_time,"%H:%M:%S")
print("Starting time:",t1.time())
t2=datetime.strptime(end_time,"%H:%M:%S")
print("Ending time:",t2.time())
diff= t2-t1
print(f"The 320Time difference is {diff.total_seconds()}seconds")

