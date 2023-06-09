# fresh-deps

## Installation

```shell
$ pip3 install git+https://gitlab.2gis.ru/pychapter/fresh-deps#egg=fresh-deps
```

## Usage

```shell
$ fresh-deps requirements.in --gitlab-project-id=<id> --gitlab-private-token=<token>
```

### GitLab CI

Add [job](https://docs.gitlab.com/ee/ci/jobs/) and create [scheduled pipeline](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)

```yml
stages:
  - update_dependencies

fresh_deps:
  stage: update_dependencies
  image: docker-hub.2gis.ru/pychapter/fresh-deps:1.0.0
  variables:
    CI_PRIVATE_TOKEN: $GITLAB_PRIVATE_TOKEN
  script:
    - fresh-deps requirements.in
  only:
    - schedules
```

https://gitlab.2gis.ru/pychapter/docker-images/-/tree/master/fresh-deps
