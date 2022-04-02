# backup-quota-checker
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FUnknown-Technology-Solutions%2Fbackup-quota-checker.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FUnknown-Technology-Solutions%2Fbackup-quota-checker?ref=badge_shield)


A webserver that checks backup quotas for our clients

An example cURL command to interact with the API:
`curl -X POST http://127.0.0.1:8080/authenticated/read_quota -H 'Content-Type: application/json' --data '{"username":"echoZulu","key":"BarFoo"}'`


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FUnknown-Technology-Solutions%2Fbackup-quota-checker.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FUnknown-Technology-Solutions%2Fbackup-quota-checker?ref=badge_large)