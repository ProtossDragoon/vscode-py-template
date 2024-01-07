# vscode-py-template

## 사용 가이드

1. 프로젝트의 이름을 정해 `project` 디렉토리의 이름을 변경합니다
    - NOTE: `Makefile`의 `PROJECT` 변수값을 이에 맞게 변경합니다.
2. 가상환경을 준비하고 활성화한 다음 `make install` 명령을 실행합니다.
3. `Makefile`은 다음과 같은 기능을 가지고 있습니다.
    - `make lint`
        - 린터는 구글 스타일 가이드 `pylintrc`를 `pylint`에 물려 사용합니다.
        - `.vscode` 설정을 사용하려면 `pylint` 익스텐션을 설치하세요.
    - `make test` (테스트는 `unittest`를 사용합니다.)
        - `test_*.py` 와 `*_test.py` 패턴을 모두 지원합니다.
        - 테스트 파일이 존재하는 위치까지 `__init__.py` 로 연결되어 있어야 합니다.
    - `make format`
        - 포매터는 google의 `yapf`를 사용합니다.
        - `yapf` 포매터의 기본 세팅에 `.style.yapf` 파일에 명시된 옵션을 오버라이딩해 코드를 포매팅합니다.
        - `.vscode` 설정을 사용하려면 `yapf` 익스텐션을 설치하세요.
