# backup-quota-checker

A webserver that checks backup quotas for our clients

An example cURL command to interact with the API:
`curl -X POST http://127.0.0.1:8080/authenticated/read_quota -H 'Content-Type: application/json' --data '{"username":"echoZulu","key":"BarFoo"}'`
