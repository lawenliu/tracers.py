from .tracer import Tracer
from algorithm_visualizer.types import Serializable


class LogTracer(Tracer):
    def set(self, log: Serializable):
        self.command("set", log)

    def print(self, message: Serializable):
        self.command("print", message)

    def println(self, message: Serializable):
        self.command("println", message)

    def printf(self, format: str, *args: Serializable):
        self.command("printf", format, *args)
