"""CLI interface for cli_gw project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import sys
import docker

from .logging import *
from .containers import ContainerRun



def lookup(prompt: list[str]) -> list[ContainerRun]:
    return [ContainerRun(
        image="cytopia/ansible:latest",
        entrypoint="ansible --version"
    )]

def apply(client, run: ContainerRun):
    container = client.containers.run(
                image=run.image, 
                entrypoint=run.entrypoint,
                detach=True
            )
    for line in container.logs(stream=True):
            line = line.decode("utf-8").strip()
            info(line)
    container.wait()
    log.debug("container ended.")

    return {} #TODO

def apply_all(runs: list[ContainerRun]):
    client = docker.from_env()
    [apply(client, run) for run in runs]
    

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m cli_gw` and `$ cli_gw `.

    This is your program's entry point.

    1- Parse the command line
    2- Identify the plugins to activate
       $ rh ansible version
       ? rh-ansible-version ?
       ? rh-ansible ! -> (JSON vs FFI) <- plugin
       ? rh-ansible.Containerfile !
         [ansible --version]

       $ rh openshift create cluster gitops/aws/...
         .....
        [build config, validate environment, deploy, post-config, verify]

    3- Build execution plan
    4- Invoke the container engine


    """
    info("This will do something!!!")
    prompt = sys.argv[1:]
    plan = lookup(prompt)
    apply_all(plan)
    info(prompt)
