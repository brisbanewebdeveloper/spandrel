from spandrel import ModelLoader
from spandrel.architectures.GFPGAN import GFPGANv1Clean

from .util import ModelFile, disallowed_props


def test_GFPGAN_1_2(snapshot):
    file = ModelFile.from_url(
        "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.2.pth"
    )
    model = ModelLoader().load_from_file(file.path)
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, GFPGANv1Clean)


def test_GFPGAN_1_3(snapshot):
    file = ModelFile.from_url(
        "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
    )
    model = ModelLoader().load_from_file(file.path)
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, GFPGANv1Clean)


def test_GFPGAN_1_4(snapshot):
    file = ModelFile.from_url(
        "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth"
    )
    model = ModelLoader().load_from_file(file.path)
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, GFPGANv1Clean)
