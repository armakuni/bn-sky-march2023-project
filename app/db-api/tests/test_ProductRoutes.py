from .fakeDatabase import FakeDB
from src.routeHandlers import ProductRoutes


def test_products_with_id():
    # arrange
    db = FakeDB(
        [
            [1, "Psychadelic snorkling kit", 49.99, 5, None],
            [
                2,
                "Pirate tennis gear",
                19.99,
                10,
                "http://sillyimages.com/pirate-tennis.png",
            ],
        ]
    )
    productRoutes = ProductRoutes(db)
    # act
    result = productRoutes.product(2)
    # assertion
    assert result == {
        "id": 2,
        "name": "Pirate tennis gear",
        "price": 19.99,
        "quantity": 10,
        "imageurl": "http://sillyimages.com/pirate-tennis.png",
    }


def test_products():
    # arrange
    db = FakeDB(
        [
            [1, "Psychadelic snorkling kit", 49.99, 5, None],
            [
                2,
                "Pirate tennis gear",
                19.99,
                10,
                "http://sillyimages.com/pirate-tennis.png",
            ],
        ]
    )
    productRoutes = ProductRoutes(db)
    # act
    result = productRoutes.products()
    # assertion
    assert result == [
        {
            "id": 1,
            "name": "Psychadelic snorkling kit",
            "price": 49.99,
            "quantity": 5,
            "imageurl": None,
        },
        {
            "id": 2,
            "name": "Pirate tennis gear",
            "price": 19.99,
            "quantity": 10,
            "imageurl": "http://sillyimages.com/pirate-tennis.png",
        },
    ]
