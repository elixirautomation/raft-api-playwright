#### Run Tests with Specific Test Group

```sh
py.cleanup -p && py.test -s -m reqres --alluredir ExecutionReports/
```


#### Trigger Allure Reports

```sh
allure serve ExecutionReports
```

