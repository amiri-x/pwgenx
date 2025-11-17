from operator import indexOf
import operator
import subprocess
import sys

import pytest

from psw_generator import generator
from psw_generator.utils.get_psw import get_psw

@pytest.mark.integration
@pytest.mark.parametrize("_",range(3))
def test_no_args(_):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate"], 
                            capture_output=True, text=True)
    assert result.returncode == 0
    prefex= "Password: "
    assert result.stdout.startswith(prefex) # does the result contains the prefex

    psw = get_psw(result.stdout)
    assert len(psw) == 8

    assert any(c.isdigit() for c in psw), "passowrd has no digits"
    assert any(c.isalpha() for c in psw), "password has no alaphbet"
    assert any(c in generator.SAFE_SYMBOLS for c in psw), "password has no specified symbol"    




@pytest.mark.integration
@pytest.mark.parametrize("len",[3, -4, 0, 129, 500, -2309, 2342])
def test_invalid_len_int(len):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "-l", str(len)], 
                            capture_output=True, text=True)
    assert result.returncode != 0
    assert f"Invalid length for password: {len}" in result.stdout
    assert "Length should be in range 4-128." in result.stdout

@pytest.mark.integration
@pytest.mark.parametrize("len",[128.1, 128.0000001, 3.9999999, 0.0, 4.0])
def test_invalid_len_float(len):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "-l", str(len)], 
                            capture_output=True, text=True)
    assert result.returncode != 0
    assert f"'{len}' is not a valid integer." in result.stderr

@pytest.mark.integration
@pytest.mark.parametrize("len",["", "abc", "\n", "?", "#"])
def test_invalid_len_str(len):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "-l", str(len)], 
                            capture_output=True, text=True)
    assert result.returncode != 0
    assert f"'{len}' is not a valid integer." in result.stderr    






@pytest.mark.integration
@pytest.mark.parametrize("_",range(3))
def test_only_digits(_):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "--only-digits" ],
                            capture_output=True, text=True)
    assert result.returncode == 0
    prefex= "Password: "
    assert result.stdout.startswith(prefex) # does the result contains the prefex
    psw = get_psw(result.stdout)

    assert len(psw) == 8

    assert any(c.isdigit() for c in psw), "passowrd has no digits"
    assert not any(c.isalpha() for c in psw), "password has alaphbet"
    assert not any(c in generator.SAFE_SYMBOLS for c in psw), "password has specified symbol"

@pytest.mark.integration
@pytest.mark.parametrize("_",range(3))
def test_no_symbol_only_digits(_):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "--no-symbol","--only-digits" ],
                            capture_output=True, text=True)
    assert result.returncode == 0
    prefex= "Password: "
    assert result.stdout.startswith(prefex) # does the result contains the prefex
    psw = get_psw(result.stdout)

    assert len(psw) == 8

    assert any(c.isdigit() for c in psw), "passowrd has no digits"
    assert not any(c.isalpha() for c in psw), "password has alaphbet"
    assert not any(c in generator.SAFE_SYMBOLS for c in psw), "password has specified symbol"






@pytest.mark.integration
@pytest.mark.parametrize("_",range(3))
def test_no_symbols(_):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "--no-symbols" ],
                            capture_output=True, text=True)
    assert result.returncode == 0
    prefex= "Password: "
    assert result.stdout.startswith(prefex) # does the result contains the prefex
    psw = get_psw(result.stdout)

    assert len(psw) == 8

    assert any(c.isdigit() for c in psw), "passowrd has no digits"
    assert any(c.isalpha() for c in psw), "password has no alaphbet"
    assert not any(c in generator.SAFE_SYMBOLS for c in psw), "password has specified symbol"    



@pytest.mark.integration
@pytest.mark.parametrize("psw_len",[4, 5, 8, 12, 16, 32, 64, 128])
def test_best_case(psw_len):
    result = subprocess.run([sys.executable, "-m", "psw_generator.generate", "-l" , str(psw_len)],
                            capture_output=True, text=True)
    assert result.returncode == 0
    prefex= "Password: "
    assert result.stdout.startswith(prefex) # does the result contains the prefex
    psw = get_psw(result.stdout)


    assert len(psw) == psw_len

    assert any(c.isdigit() for c in psw), "passowrd has no digits"
    assert any(c.isalpha() for c in psw), "password has no alaphbet"
    assert any(c in generator.SAFE_SYMBOLS for c in psw), "password has no specified symbol"    

    