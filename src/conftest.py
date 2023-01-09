import pytest
from playwright.sync_api import Playwright
from py.xml import html
from datetime import datetime

htmlImg = ''
htmlVideo = ''
baseUrl = None


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(str(datetime.utcnow()), class_='col-time'))
    cells.pop()

@pytest.fixture()
def context(playwright: Playwright):
    
    context = playwright.chromium.launch(
        channel="chrome",
        headless=True,
        slow_mo=100,
        timeout=20000,
    )
    context = context.new_context(record_video_dir="src/report/videos/")

    yield context

    context.close()


@pytest.fixture
def api_request_context(playwright: Playwright):    
    context = playwright.request.new_context(
        base_url= baseUrl
    )
    yield context
    context.dispose()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.html(htmlImg))
        extra.append(pytest_html.extras.html(htmlVideo))
        report.extra = extra



def pytest_addoption(parser):
    parser.addoption("--MTs", action="store")

@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()  
    return name_value