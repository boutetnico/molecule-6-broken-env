import pytest

import os

def test_env_var_exists(host):
    var = os.environ.get("TEST_VAR_FOO")
    assert var == "BAR"
