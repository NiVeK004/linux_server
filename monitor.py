import psycopg2
import psutil
from datetime import datetime

# Database tilkobling

kobling = psycopg2.connect(
	dbname="server_monitor",
	user="monitor_admin",
	password="nftn47",
	host="localhost"
)
cursor = kobling.cursor()

# Samle systemdata

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

# Innføre data i databasen
cursor.execute(
	"INSERT INTO metrics (cpu_usage, memory_usage, disk_usage, network_traffic) VALUES (%s, %s, %s,%s)",
	(cpu, memory, disk, network)
)
kobling.commit()

# Lukke tilkobling

cursor.close()
kobling.close()

print(f"[{datetime.now()}] Data lagret: CPU={cpu}%, Minne={memory}%, Disk={disk}%, Nettverk={network} bytes")
