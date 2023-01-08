import allure

from selene import by, be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.testcase('www.zdes_vse_testcases.com', name='Проверка текста в Github')
@allure.label('owner', 'Ivanov Ivan')
@allure.link('https://github.com', name='Main site')
def test_decorator(size_browser):
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#57')


@allure.step('Открываем страницу GitHub')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo} по названию')
def search_for_repository(repo):
    browser.element('.header-search-input').send_keys(
        'eroshenkoam/allure-example').submit()


@allure.step('Переходим в репозиторий {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем вкладку Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие текста {number} во всех Issues')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
