import time
import redis

r = redis.Redis(host="redis", port=6379)

print("Worker started and waiting for jobs...")

while True:
    job = r.lpop("jobs")

    if job:
        job_id = job.decode()
        print(f"Processing job {job_id}")
        time.sleep(2)  # simulate work
        print(f"Done: {job_id}")
    else:
        print("No jobs found, waiting...")
        time.sleep(3)
