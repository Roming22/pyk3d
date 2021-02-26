from pyk3d import __commit__, __version__


def test_version():
    assert __version__ == "0.0.dev0"
    assert __commit__ == "localdev"
