from practice import formatted_name

def test_formatted_name():
    formal_name = formatted_name('harsh','tomar')
    assert formal_name == 'Harsh Tomar'