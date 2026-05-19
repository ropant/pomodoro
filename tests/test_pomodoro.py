from pomodoro import calCulTemps


def test_cas_normal():
    # 90 secondes = 1 minute et 30 secondes
    assert calCulTemps(90) == (1, 30)


def test_zero_secondes():
    # 0 secondes = 0 minute et 0 secondes
    assert calCulTemps(0) == (0, 0)


def test_une_minute_pile():
    # 60 secondes = 1 minute et 0 secondes
    assert calCulTemps(60) == (1, 0)


def test_valeur_pomodoro():
    # 1500 secondes = 25 minutes (un vrai pomodoro)
    assert calCulTemps(1500) == (25, 0)


def test_pause_courte():
    # 300 secondes = 5 minutes (pause standard)
    assert calCulTemps(300) == (5, 0)
