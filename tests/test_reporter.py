from reporter import header

def test_reporter():
    assert True

def test_create_header():
    author = {
    'firstname' : 'Miles',
    'lastname' : 'Davis'}

    author2 = {
            'firstname' : 'John',
            'lastname' : 'Mike'
        }

    aut = [author, author2]
    header_test = header.create_header(aut)
    assert "Miles" in header_test
    