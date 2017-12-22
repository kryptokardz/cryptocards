# CryptoMonsters

A card trading game that uses blockchain technology in order for players to get cards. Each card would then be owned securely by the player in their digital wallet. Players would get cards either by "mining" for them, trading with other players, or melding two cards to create a new card. Each card would have specific attribute genetics that could be passed on to their children.

This is a work in progress and hopefully we will remember to keep this updated as we move along.


## Authors
**[Cody Dibble](https://www.github.com/hcodydibble)** -
**[Mark Reynoso](https://www.github.com/markreynoso)** -
**[John Jensen](https://www.github.com/thejohnjensen)** -
**[Chaitanya Narukulla](https://www.github.com/chaitanyanarukulla)**-

## Artist
Artwork by Travis Koon
Backstories by Matthew Cornmesser
Mining goblins by [Dillon Wall](https://www.dillonwall.com)


## Backstory


## Getting Started

Clone this repository to your local machine.
```
$ git clone https://github.com/kryptokardz/cryptocards.git
```

Once downloaded, change directory into the `cryptocards` directory.
```
$ cd cryptocards
```

Begin a new virtual environment with Python 3 and activate it.
```
cryptocards $ python3 -m venv ENV
cryptocards $ source ENV/bin/activate
```

Install the application requirements with [`pip`](https://pip.pypa.io/en/stable/installing/).
```
(ENV) cryptocards $ pip install -r requirements.txt
```

Create a [Postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides) database for use with this application.
```
(ENV) cryptocards $ createdb cryptomonsters
```

Export environmental variables pointing to the location of database, your username, hashed password, and secret
```
(ENV) cryptocards $ export SECRET_KEY='secret'
(ENV) cryptocards $ export DB_NAME='cryptomonsters'
(ENV) cryptocards $ export DB_USER='(your postgresql username)'
(ENV) cryptocards $ export DB_PASS='(your postgresql password)'
(ENV) cryptocards $ export DB_HOST='localhost'
(ENV) cryptocards $ export DEBUG='True'
```

Then initialize the database with the `migrate` command from `manage.py`
```
(ENV) cryptocards $ python cryptomonsters/manage.py migrate
```

Once the package is installed and the database is created, start the server with the `runserver` command from `manage.py`
```
(ENV) cryptocards $ python cryptomonsters/manage.py runserver
```

Application is served on http://localhost:8000

## Testing
You can test this application by first exporting an environmental variable pointing to the location of a testing database, then running the `test` command from `manage.py`.
```
(ENV) cryptocards $ export TEST_DB='cryptotests'
(ENV) cryptocards $ python cryptomonsters/manage.py test cryptomonsters
```

## Deploying
You can deploy this application to AWS using Ansible.

```[Sign Up for AWS](https://aws.amazon.com/)

[Setting Up with Amazon EC2](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html)

[Launch an Instance]
(http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
```

Create a `hosts` file in the root of `cryptocards`
```
[us-west-2]
(your EC2 public IP address)

[us-west-2:vars]
ansible_ssh_user=(your EC2 user)
ansible_ssh_private_key_file=/path/to/your/key.pem

server_dns=(your EC2 public DNS)
secret_key='secret'
db_name='(your RDS database name)'
db_host='(your RDS endpoint)'
db_user='(your RDS username)'
db_pass='(your RDS password)'
test_db='test_cryptomonsters'
allowed_hosts='(your EC2 public DNS) (your EC2 public IP address)'

aws_storage_bucket_name='(your S3 bucket name)'
aws_access_key_id='(your IAM user access key id)'
aws_secret_access_key='(your IAM user secret access key)'

admin_email='(your email address for admin)'
admin_email_host='(host for your admin email)'
admin_email_pass='(password for your admin email)'
```

Deploy the application with `ansible-playbook`
```
(ENV) cryptocards $ ansible-playbook -i hosts playbook/cryptomonsterswire_playbook.yml
```

## Architecture
Built with Python Django and Bootstrap framework. Tested through Django testing suite.
