import allure
from selene import by, be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag('web', 'api')
@allure.severity(Severity.BLOCKER)
@allure.testcase('www.zdes_vse_testcases.com', name='Проверка текста в Github')
@allure.label('owner', 'Ivanov Ivan')
@allure.link('https://github.com', name='Main site')
def test_selene_find_issue(size_browser):
    browser.open('https://github.com')

    browser.element('.header-search-input').send_keys(
        'eroshenkoam/allure-example').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#57')).should(be.visible)



