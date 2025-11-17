
import pytest

from psw_generator import generator

@pytest.mark.unit
@pytest.mark.parametrize("len", [3, 2, 1, 0, -1, -3, -0, 0.0, -0.4, -128])
def test_generate_small_vlaue(len):
    with pytest.raises(ValueError):
        generator.generate(len)

@pytest.mark.unit
@pytest.mark.parametrize("len", [10000, 100000000000000,129, 230])
def test_generate_big_vlaue(len):
    with pytest.raises(ValueError):
        generator.generate(len)

@pytest.mark.unit
@pytest.mark.parametrize("len", [124.0001, 128.1,  128.000001, 543.4])
def test_generate_float_vlaue(len):
    with pytest.raises(ValueError):
        generator.generate(len)

@pytest.mark.unit
@pytest.mark.parametrize("len", ['az', "abc", ".", "4F", "", " ", "\t", "0", "123"])
def test_generate_str_value(len):
    with pytest.raises(TypeError):
        generator.generate(len)



@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_only_digigts(_):
    psw = generator.generate(128, no_symbols=True, only_digits=True)
    assert len(psw) == 128
    assert psw.isdigit, "password contains non-digit chars"

@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_only_digigts_with_four(_):
    psw = generator.generate(4, no_symbols=True, only_digits=True)
    assert len(psw) == 4
    assert psw.isdigit, "password contains non-digit chars"

@pytest.mark.unit    
@pytest.mark.parametrize("_", range(50))
def test_generate_return_only_digigts_even_no_symbols_is_false(_):
    psw = generator.generate(16, only_digits=True) # no_symbols == False
    assert len(psw) == 16
    assert psw.isdigit, "password contains non-digit chars"


@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_only_alpha(_):
    psw = generator.generate(128, no_symbols=True) # only_digits == False
    assert len(psw) == 128
    assert psw.isalpha, "password contains non-alphabet chars"

@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_only_alpha_with_four(_):
    psw = generator.generate(4, no_symbols=True) # only_digits == False
    assert len(psw) == 4
    assert psw.isalpha, "password contains non-alphabet chars"


@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_psw(_):
    psw = generator.generate(128) # nosymbols == False, only_digits == False
    assert len(psw) == 128
    assert any(c.isdigit for c in psw), "passowrd has no digits"
    assert any(c.isalpha for c in psw), "password has no alaphbet"
    assert any(c in generator.SAFE_SYMBOLS for c in psw), "password has no specified symbol"

@pytest.mark.unit
@pytest.mark.parametrize("_", range(50))
def test_generate_return_psw_with_four(_):
    psw = generator.generate(4) # nosymbols == False, only_digits == False
    assert len(psw) == 4
    assert any(c.isdigit for c in psw), "passowrd has no digits"
    assert any(c.isalpha for c in psw), "password has no alaphbet"
    assert any(c in generator.SAFE_SYMBOLS for c in psw), "password has no specified symbol"    