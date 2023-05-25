from command.command import Command


def test_answer():
    assert "test" == Command(name="Test").name


n = Command(name="Test")
print(n.name)
