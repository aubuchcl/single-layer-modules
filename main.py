import sys
sys.path.append("./mod-demo/")
sys.path.append("./mod-test/")

import demo
import test


def recursive_success():
    demo_output = f"demo module: ${demo.talk()}"
    test_output = f"test module: ${test.testOutput()}"


recursive_success()