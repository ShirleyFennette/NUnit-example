# Проверка отдельных Launch в TestOps из GitHub Actions

Это самостоятельный демонстрационный проект: 5 unit-тестов и 2 функциональных
сценария расчёта корзины. Внешнее приложение и браузер не нужны.

## Загрузка

Скопируйте **содержимое этой папки**, включая скрытую `.github`, в корень вашего
GitHub-репозитория. Git, коммиты и push здесь не выполнялись.

В Settings → Secrets and variables → Actions добавьте:

- Secret `ALLURE_ENDPOINT`: URL вашего TestOps без завершающего `/`.
- Secret `ALLURE_TOKEN`: API-токен с доступом к проекту.
- Variable `ALLURE_PROJECT_ID`: ID проекта; по умолчанию `72`.

Hosted runner GitHub должен иметь сетевой доступ к TestOps.
Запуск: push либо Actions → Verify separate TestOps launches → Run workflow.
`workflow_dispatch` также можно вызвать через GitHub API.

## Что проверяет workflow

`unit-tests` → `func-test` → `verify-launches`.
Функциональная джоба запускается после успешной unit-джобы.
Обе используют allurectl **2.18.0** — версию из исходного обращения.
Для другой версии измените `ALLURECTL_VERSION` в workflow.

UID формируется как `GITHUB_RUN_ID-GITHUB_RUN_ATTEMPT-GITHUB_JOB`.
Джобы получают разные UID; повторный запуск workflow — новую попытку.
Явные `ALLURE_LAUNCH_ID` и `ALLURE_JOB_RUN_ID` сбрасываются.
Общий Job UID не переопределяется: проверяем именно разделение по Job Run UID.

**Гипотеза:** allurectl сохраняет переданный `ALLURE_JOB_RUN_UID` при определении
GitHub Actions. Исходники клиента не проверены. Реальную проверку выполняет
`verify-launches`: получает Launch ID через `allurectl job-run env` от обеих
джоб и требует непустые разные ID. При совпадении или отсутствии ID workflow
завершается ошибкой. Смотрите также строки `Job Run uid` в логах `watch`.
Локальное прохождение pytest не подтверждает разделение на сервере.

В артефактах каждой джобы сохраняются Allure results. Полное окружение и токен
скрипт не печатает. Проверка сравнивает серверные ID, но не проверяет состав
результатов через API: в TestOps дополнительно проверьте 5 unit и 2 functional
результата в соответствующих Launch.

Привязка к DEMO-1 и интеграции 344 из исходного примера не включена: она требует
настроенной интеграции конкретного сервера и не относится к проверке разделения.

## Локальная проверка без TestOps

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest --alluredir=allure-results
```

Основные файлы: `.github/workflows/testops.yml`, `scripts/run_suite.py`,
`scripts/verify_launches.py`, `tests/unit/`, `tests/functional/`.
