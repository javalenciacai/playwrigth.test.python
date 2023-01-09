import pytest
from playwright.sync_api import Playwright

htmlImg = ''
htmlVideo = ''
baseUrl = None

@pytest.fixture()
def context(playwright: Playwright):
    
    context = playwright.chromium.launch(
        channel="chrome",
        headless=True,
        slow_mo=0,
        timeout=20000,
    )
    context = context.new_context(record_video_dir="src/report/videos/")

    yield context

    context.close()


@pytest.fixture
def api_request_context(playwright: Playwright):    
    context = playwright.request.new_context(
        base_url= baseUrl,
        extra_http_headers={
            "Content-Type": "application/json",
            "Authorization": "Token my-api-token",
        },
    )
    yield context
    context.dispose()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.html(htmlImg))
        extra.append(pytest_html.extras.html(htmlVideo))
        report.extra = extra
    