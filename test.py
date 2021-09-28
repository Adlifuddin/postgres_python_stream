import select
import psycopg2
import psycopg2.extensions

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="990901075399adli")
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

curs = conn.cursor()
curs.execute("LISTEN notify;")

print("Waiting for notifications on channel 'notify'")
while True:
    if select.select([conn],[],[],5) == ([],[],[]):
        print("Timeout")
    else:
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print(f"Got NOTIFY: , {notify.pid}, {notify.channel}, {notify.payload}")