from processor import clean_id, merge_name
def test_clean_id():
    assert clean_id("cc-83.46.278-341")=="8346278341"

def test_merge_name():
    assert merge_name("Esteban", "Hoyos")=="Esteban Hoyos"