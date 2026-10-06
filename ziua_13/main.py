from functii import este_par


def test_este_par_cu_numar_par():
    assert este_par(4) is True


def test_este_par_cu_numar_impar():
    assert este_par(7) is False