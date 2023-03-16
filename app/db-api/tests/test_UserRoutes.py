from src.routeHandlers import UserRoutes


class FakeDBCursor(list):
    def __init__(self, results):
        super().__init__(results)

    def execute(self, sql):
        pass

    def close(self):
        pass


class FakeDBConnection:
    def __init__(self, fakeResults):
        self.fakeResults = fakeResults

    def cursor(self):
        return FakeDBCursor(self.fakeResults)

    def close(self):
        pass


class FakeDB:
    def __init__(self, fakeResults):
        self.fakeResults = fakeResults

    def readConnection(self):
        return FakeDBConnection(self.fakeResults)


def test_users():
    # arrange
    db = FakeDB([[1, "Andrew"], [2, "Gracie"]])
    userRoutes = UserRoutes(db)
    # act
    result = userRoutes.users()
    # assertion
    assert result == [{"id": 1, "username": "Andrew"}, {"id": 2, "username": "Gracie"}]
