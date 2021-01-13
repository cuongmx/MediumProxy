# Medium Proxy

Medium Proxy is an application written to run in heroku app. This application will run as a reversed proxy to your medium page. By that way, you can customize the personal domain for you Medium page.

## Features
1. Reversed proxy for Medium page
2. Fix the 500 error bug by remove all javascript listener of Medium page.

## Installation

1. Deploy app in your Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cuongmx/MediumProxy)

2. Setup customize domain to your Heroku (use [this guide](https://devcenter.heroku.com/articles/custom-domains))

3. If you wanna run in https, please let your domain behide the Cloudflare

## Demo
https://m.cuong.mx is the customize domain for https://cuongmx.medium.com

## License
Copyright (c) 2021, [cuongmx](https://cuong.mx). MIT License.
