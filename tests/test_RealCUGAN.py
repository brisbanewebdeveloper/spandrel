from spandrel.architectures.RealCUGAN import UpCunet2x, UpCunet3x, UpCunet4x, load

from .util import (
    ModelFile,
    TestImage,
    assert_image_inference,
    assert_loads_correctly,
    assert_size_requirements,
    disallowed_props,
)


def test_RealCUGAN_load():
    assert_loads_correctly(
        load,
        lambda: UpCunet2x(in_channels=3, out_channels=3),
        lambda: UpCunet2x(in_channels=1, out_channels=4),
        lambda: UpCunet2x(pro=True),
        lambda: UpCunet3x(in_channels=3, out_channels=3),
        lambda: UpCunet3x(in_channels=1, out_channels=4),
        lambda: UpCunet3x(pro=True),
        lambda: UpCunet4x(in_channels=3, out_channels=3),
        lambda: UpCunet4x(in_channels=1, out_channels=3),
        lambda: UpCunet4x(pro=True),
        condition=lambda a, b: (a.is_pro == b.is_pro),
    )


def test_size_requirements():
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1VtBY4ZEebEiYL-IZRGJ61LUDCSRvkdoC/view?usp=sharing",
        name="up2x-latest-no-denoise.pth",
    )
    assert_size_requirements(file.load_model())

    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1DfB-tMUKU_3NwQuM9Z0ZGYPhfLmzkDHb/view?usp=sharing",
        name="up3x-latest-no-denoise.pth",
    )
    assert_size_requirements(file.load_model())

    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1Y7SGNuivVjPf1g6F3IMvTsqt64p_pTeH/view?usp=sharing",
        name="up4x-latest-no-denoise.pth",
    )
    assert_size_requirements(file.load_model())


def test_RealCUGAN_2x(snapshot):
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1VtBY4ZEebEiYL-IZRGJ61LUDCSRvkdoC/view?usp=sharing",
        name="up2x-latest-no-denoise.pth",
    )
    model = file.load_model()
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, UpCunet2x)
    assert_image_inference(
        file,
        model,
        [TestImage.SR_32, TestImage.SR_64],
    )


def test_RealCUGAN_3x(snapshot):
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1DfB-tMUKU_3NwQuM9Z0ZGYPhfLmzkDHb/view?usp=sharing",
        name="up3x-latest-no-denoise.pth",
    )
    model = file.load_model()
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, UpCunet3x)
    assert_image_inference(
        file,
        model,
        [TestImage.SR_32, TestImage.SR_64],
    )


def test_RealCUGAN_4x(snapshot):
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1Y7SGNuivVjPf1g6F3IMvTsqt64p_pTeH/view?usp=sharing",
        name="up4x-latest-no-denoise.pth",
    )
    model = file.load_model()
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, UpCunet4x)
    assert_image_inference(
        file,
        model,
        [TestImage.SR_32, TestImage.SR_64],
    )


def test_RealCUGAN_2x_pro(snapshot):
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/10QOxPsGmWyBTLK2ATTR9FzRNaXWSEfrt/view?usp=sharing",
        name="pro-no-denoise-up2x.pth",
    )
    model = file.load_model()
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, UpCunet2x)
    assert_image_inference(
        file,
        model,
        [TestImage.SR_32, TestImage.SR_64],
    )


def test_RealCUGAN_3x_pro(snapshot):
    file = ModelFile.from_url(
        "https://drive.google.com/file/d/1jTmhjMwusUsRp2h9lsMZtTM9n8UL6p_V/view?usp=sharing",
        name="pro-no-denoise-up3x.pth",
    )
    model = file.load_model()
    assert model == snapshot(exclude=disallowed_props)
    assert isinstance(model.model, UpCunet3x)
    assert_image_inference(
        file,
        model,
        [TestImage.SR_32, TestImage.SR_64],
    )
