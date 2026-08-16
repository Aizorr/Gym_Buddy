import urllib.request
import os
import json
from datetime import datetime
plan = ["1: Chest + Biceps",
        "2: Back + Triceps",
        "3: Legs + Shoulders",
        "4: Running"]
today = datetime.now().strftime("%A")
print(today)
try:
    with open("stan.txt", "r") as f:
        index = int(f.read().strip())
except FileNotFoundError:
    index = 0
today_plan = plan[index]
print(today_plan)
new_index = (index + 1) % len(plan)
with open("stan.txt", "w") as f:
    f.write(str(new_index))
url = os.getenv("DISCORD_WEBHOOK_URL")
if not url:
    print("No Discord Webhook URL found")
    exit()
data = {"content": f"Dzisiejszy trening: {today_plan}"}
json_data = json.dumps(data).encode("utf-8")
header = {"User-Agent": "Mozilla/5.0","Content-Type": "application/json"}
req = urllib.request.Request(url, data=json_data,headers=header)
urllib.request.urlopen(req)
