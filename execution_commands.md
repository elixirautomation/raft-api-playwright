#### Run Tests with Specific Group

```sh
py.cleanup -p && py.test -m reqres --alluredir ExecutionReports/
```


#### Trigger Allure Reports

```sh
allure serve ExecutionReports
```

