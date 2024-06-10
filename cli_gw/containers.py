from dataclasses import dataclass

@dataclass
class ContainerRun:
    """Execution of a container"""
    image: str
    entrypoint: str | list