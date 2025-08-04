from .logline_grammar import *
from .logline_parser import LogLineParser
from .logline_engine import LogLineEngine

# Example usage:
# engine = LogLineEngine()
# with open("core/priority.lll") as f:
#     engine.load_rule(f.read())
# engine.evaluate("PRIORITY-IDEA", context)