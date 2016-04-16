
"""
This is a singleton patterns.
The benefit is that we only needs to import 
dclient into a module that will work with 
the docker client.

Ex:
from dclient import dclient as cli
"""
from sys import platform

if platform == "linux" or platform == "linux2":
    from docker import Client
    cli = Client(base_url='unix://var/run/docker.sock')
else:
    import docker
    cli = docker.from_env(assert_hostname=False)


# Every running container will be put here as "<title>:<id>" pairs
workers = {}

def list_all():
    return cli.containers(all=True)

def execute(container_title, code, target):
    container = cli.create_container(image=container_title,
                         command=str("-c {} -t {}".format(code, target)))

    workers[container_title] = container.get('Id')
    print(cli.start(container.get('Id')))

def check_results():
    results = []
    for title, id in workers.iteritems():
        res = cli.logs(id)
        if res:
            results.append({title:res})

    return results

def kill_all():
    for worker, id in workers:
        cli.stop(id)




