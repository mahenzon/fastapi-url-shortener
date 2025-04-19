from os import getenv

import pytest

if getenv("TESTING") != "1":
    pytest.exit(
        "Environment is not ready for testing",
    )
