import time

# currentTime = int(time.time())
# print(f"start time: \t{currentTime}")
# time.sleep(5)
# print(f"end time: \t{time.time()}")


# Print time every 5 seconds
interval = 5
startTime = time.time() - interval

# while True:
#     currentTime = time.time()
#     if (startTime + interval) <= currentTime:
#         print(currentTime)
#         startTime = currentTime

while (startTime + interval) <= time.time():
    print(time.time())
    startTime = time.time()

