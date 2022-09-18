import pytest

htmlImg = ''
htmlVideo = ''

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