from app.history import History

def test_history_add_entry():
    history = History()
    history.add_entry("add", 1, 2, 3)
    assert len(history.history) == 1

def test_history_clear():
    history = History()
    history.add_entry("sub", 5, 2, 3)
    history.clear_history()
    assert history.history.empty

