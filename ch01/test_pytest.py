import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 2

def test_decrement_twice():
    assert inc_dec.decrement(
        inc_dec.decrement(3)) == 1
        
def test_increment_andthen_decrement():
    assert inc_dec.decrement(
        inc_dec.increment(42)) == 42