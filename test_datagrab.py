import sys

import pytest
import zdowneyproject1


@pytest.fixture
def get_data():
    import zdowneyproject1
    return zdowneyproject1.list_shows()


def test_dict(get_data):
    assert len(get_data) == 250
    assert type(get_data[1]) is dict


def test_save_data():
    demo_data = {'id': 1234, 'type': "Testable"}
    list_data = []
    list_data.append(demo_data)
    file_name = "testfile.txt"
    zdowneyproject1.save_data(list_data, file_name)
    testfile = open(file_name, 'r')
    saved_data = testfile.readlines()
    assert f"{str(demo_data)}\n" in saved_data