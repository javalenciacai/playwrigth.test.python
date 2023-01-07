import pytest
from playwright.sync_api import Playwright

htmlImg = ''
htmlVideo = ''

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
    