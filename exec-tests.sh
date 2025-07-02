export ALLURE_TOKEN=67aad6fa-966a-49ef-a598-e572b3e030f9
export ALLURE_ENDPOINT=http://testing.qatools.cloud
export ALLURE_PROJECT_ID=1605
export ALLURE_LAUNCH_NAME="checking various attachments"
export ALLURE_RESULTS=allure-results

./allurectl watch -- pytest ./tests --alluredir=${ALLURE_RESULTS}
--endpoint http://testing.qatools.cloud
--token 67aad6fa-966a-49ef-a598-e572b3e030f9 
