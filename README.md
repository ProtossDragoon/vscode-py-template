# vscode-py-template

환경은 MacOS, Linux 를 기준으로 합니다.

## 셋업

1. 프로젝트의 이름을 정해 `myproject`(가명) 디렉토리의 이름을 변경합니다
    - 이때 `myproject` 는 파이썬에서 임포트가능한 이름이어야 합니다. (e.g. `tensorflow`, `torch`, `Flask`)
    - 소문자만으로 이루어진 단일단어로 구성하세요.  *'_' 같은 것이 덕지덕지 붙으면 멋이 없어요.*
    - `Makefile`의 `PROJECT` 변수값을 동일하게 변경합니다.
    - `pyproject.yaml` 의 `name` 변수값, `src` 변수값을 동일하게 변경합니다.
2. 가상환경을 준비하고 활성화한 다음 `make install` 명령을 실행합니다.
    - `make install` 은 개발 모드로 패키지를 설치합니다.
    - 개발 모드로 설치하는 것이기 때문에, 가상환경의 `site-package` 디렉토리에 소프트 링크를 거는 방식으로 작동합니다.
    - 동일한 가상환경을 사용하는 프로젝트에서 이 `myproject`(가명) 을 임포트해 사용할 수 있습니다. 이때, 현재 프로젝트 폴더 내에서 파일을 수정하면, 링크가 걸려 있기 때문에 `myproject` 를 사용하는 다른 프로젝트에서도 별도의 업데이트 없이 곧바로 수정내용이 반영됩니다. 물론, 이미 특정 모듈을 불러왔다면 파이썬을 닫았다가 다시 켜야 합니다.
3. 디스코드를 사용하는 경우, 깃허브 액션 secret 변수 `DISCORD_WEBHOOK_URL` 을 지정합니다.
    - 알림을 보내고 싶은 디스코드 채널의 웹훅 URL을 값으로 등록합니다.
    - 관련 액션은 [ci-discord-noti.yml](.github/workflows/ci-discord-noti.yml) 입니다.
4. 로거를 설정합니다.
    - `myproject/logging.yaml`의 `myproject`, `myproject/log_utils.py`의 `myproject`을 찾아 대치합니다.
