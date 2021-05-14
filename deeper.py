import sys
sys.path.append("./modules/")

import demo
import test


def recursive_success():
    demo_output = f"demo module: ${demo.talk()}"
    test_output = f"test module: ${test.testOutput()}"


