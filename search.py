import subprocess

# Creating a new container
create_command = "docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest"
subprocess.run(create_command, shell=True)

# # Starting an existing container
# start_command = "docker start -a redis-stack"
# subprocess.run(start_command, shell=True)
