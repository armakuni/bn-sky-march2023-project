from .fakeDatabase import FakeDB
from src.routeHandlers import UserRoutes


def test_users():
    # arrange
    db = FakeDB([[1, "Andrew"], [2, "Gracie"]])
    userRoutes = UserRoutes(db)
    # act
    result = userRoutes.users()
    # assertion
    assert result == [{"id": 1, "username": "Andrew"}, {"id": 2, "username": "Gracie"}]
