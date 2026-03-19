@pytest.fixture
def browser_page(request):
    browser =
    page = context.new_page()
    
    yield page