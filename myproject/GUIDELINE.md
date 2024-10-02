# GUIDELINE

## 거대구조

- 필요한 기능은 마이크로서비스로 구축한다.
- 마이크로서비스 기본 디자인 철학은 DDD(domain-driven-design)이다.

### DDD

- Domain: 가장 추상적인 비즈니스 로직, 순수 python 만으로 구현
  - domain/exception: 예외.
  - domain/entity: '고유한 식별자'를 가진 객체. (e.g. 고객, 상품)
    - NOTE: entity 는 `__eq__` 와 `__hash__` 가 구현되어야 한다.
  - domain/vo: 'value-object'로, 도메인 내의 값이나 성질을 표현함. (e.g. 돈, 위치, 날짜 등)
  - domain/aggregate: entity 와 value object의 묶음. (e.g. 주문 = 고객 + 상품 + 돈)
  - domain/service: 상태를 가지지 않는, 행위나 프로세스를 의미함. (e.g. 적용 가능한 할인 계산)
- Application: 도메인 객체, 인프라, 서드파티 라이브러리 등에 의존한 기능 구현부.
  - application/usecase: 시스템이 제공하는 기능을 유저 관점으로 구현 (e.g. 주문(시스템 관점) -> 주문하기(유저 관점))
    - application/usecase/query: R(Read) 기능
    - application/usecase/command: CUD(Create, Update, Delete) 기능
    - 이때 직접 읽고 쓰지 않고 Infrastructure 레이어를 통한 repository 패턴을 적용함.
- Infrastructure: DB, 캐싱, 로깅, 외부 API. 애플리케이션을 돕는 계층.
- Presentation: UI, CLI, 유저에게 제공되는 Restful API, 입출력 validation, 데이터 표현

## 프레임워크

- python 의존성 관리는 `pyproject.toml` 을 사용한다.
- python 빌드 프론트엔드는 `flit` 을 사용한다.
- python API 백엔드 라이브러리는 `FastAPI` 를 사용한다.
- python CLI 라이브러리는 `Typer` 를 사용한다.

## 마이크로서비스 스캐폴드 스타일

- HTTP API 엔드포인트는 `endpoint.py` 이다.
- 프론트엔드 실행파일은 `app.py` 이다.
- CLI 엔드포인트는 `cli.py` 이다.
- 이들 각각은 `python3 -m` 으로 접근 가능해야 한다.

### 기타 파일 작성 가이드

- 자료구조는 기본적으로 version2 upper 의 `pydantic` 을 사용한다.
- 비즈니스 로직용 자료 구조는 `model.py`에 작성한다.
- FastAPI 용 자료 구조는 `schema.py` 에 작성한다.
- `schema.py` 의 클래스는 `model.py` 의 클래스를 포함관계로 가지거나 래핑할 수 있다.

### 간단한 구조

- 마이크로서비스가 복잡해지면 마이크로서비스 루트 내부 구조가 고도화된다.
- 각 마이크로서비스는 플랫(flat) 스캐폴드 구조를 따른다.
- 간단한 애플리케이션의 경우 마이크로서비스 루트 내부는 다음과 같이 구성될 수 있다.
- 아래는 프로젝트 루트와 마이크로서비스 루트 사이의 관계 또한 보여준다.

```
planit # 프로젝트 루트
├── Makefile
├── README.md
├── planit
│   ├── __init__.py
│   └── { service_a } # 마이크로서비스 루트
│       ├── test
│       └── { service_a }
│           ├── GUIDELINE.md
│           ├── README.md
│           ├── domain
│           │   ├── {domain_a}
│           │   │   ├── exception.py # 만약 파일의 길이가 200줄이 넘어가면 디렉토리로 만들고 의미 단위 파일로 분리할 수 있음.
│           │   │   ├── entity.py # 만약 파일의 길이가 200줄이 넘어가면 디렉토리로 만들고 의미 단위 파일로 분리할 수 있음.
│           │   │   └── ...
│           │   └── {domain_b}
│           │       └── ...
│           ├── application
│           │   └── ...
│           └── ...
└── pyproject.toml
```

## 모든 파이썬 스크립트의 임포트 스타일

- 마이크로서비스별 상대경로를 사용하되, 마이크로서비스 내부에서는 절대경로만을 사용한다.
- 예를 들어 마이크로서비스 `A`의 프론트엔드에서 `example.py` 를 호출할 때, `from A import example` 을 사용한다.
- 만약 `examples` 디렉토리 안에 `a.py`, `b.py` 가 있는데, `a.py` 가 `b.py` 를 임포트한다면 `from A.examples import b` 를 사용한다.
- `a.py`, `b.py` 모두 `python3 -m` 으로 마이크로서비스 루트에서 접근 가능해야 하기 때문이다. (참고: 프로젝트 루트에서는 `.vscode` 설정과 `PYTHONPATH` 설정을 통해 접근한다.)

## FastAPI 엔드포인트 코드 작성 가이드

- 응답(response) 모델 정의
  - 응답 모델이란 엔드포인트의 JSON 리턴 형식이다.
  - 키-값 쌍이 하나인 응답 모델의 경우 굳이 타입을 추가해서 복잡성을 높이지 않는다.
    - 그냥 엔드포인트 레벨에서 변수명과 똑같은 키에 값을 담아 리턴하라.
    - *Pythonic! KISS!*
  - 응답 모델에 에러 정보같은 필드를 이왕이면 만들지 마라.
    - FastAPI의 `HTTPException` 클래스 `detail` 인자로 전하라.
    - 백엔드 에러 메시지는 FastAPI가 `HTTPException` 으로 보내준다.
  - 응답 모델이 복잡해지는 경우에만 `pydantic` 을 사용한다.
- 비즈니스 로직 레벨
  - 내부적으로 응답(response)모델을 사용하지 않는다.
  - 비즈니스 로직 소스코드는 네트워크를 전혀 신경쓰지 않는다.
    - 예를 들어 예외처리 시 `HTTPException` 같은 놈을 사용하지 않는다.
- 엔드포인트 레벨
  - 비즈니스 로직은 최대한 숨겨져 있어야 한다.
    - 최상위 비즈니스 로직의 간단한 분기 정도의 논리만 남겨져 있다.
  - 비즈니스 로직을 위한 데이터 모델을 응답모델로 변경하는 부분이 포함된다.
  - 비즈니스 로직에서 사용된 Exception 들을 catch 하는 부분이 포함된다.
    - 대부분 `HTTPException` 의 `status_code=500` reraise 방식으로 구현된다.
    - 서버 디버깅을 쉽게 하기 위해 `HTTPException` … `from e` 로 스택 트레이스를 남긴다.

## Streamlit 프론트엔드 코드 작성 가이드

- 앞서 언급했듯 `app.py` 에 웹 페이지가 명세된다.
- 하지만 파이썬 모듈 컨텍스트를 유지하기 위해, `cli.py` 에서 `from streamlit.web import cli` 를 호출하는 엔트리포인트로 우회하다.

## 소스코드 레벨 스타일

- 임포트 순서는 내장 모듈 -> 서드파티 모듈 -> 프로젝트 모듈이다.
  ```python
  # 내장 ('내장' 주석 작성)
  import xxx
  ### 한 줄 개행
  # 서드파티 ('서드파티' 주석 작성)
  import yyy
  ### 한 줄 개행
  # 프로젝트 ('프로젝트' 주석 작성)
  from a.b import c
  ```
- 문자열과 f-string 등 모든 문자열 표현은 작은 따옴표(small quote, ')를 사용한다.
- 모든 클래스와 함수에 docstring 을 작성한다. docstring은 큰 따옴표를 사용한다.
- docstring 은 Google 스타일을 사용한다.
- python 3.10 이상에서 지원하는 타입 힌트를 사용한다.

```python
def hello_worlds(param1: str, param2: int) -> list[str]:
    """문서. (주의 - 음슴체로 작성할 것.)

    Args:
        param1: 설명 (주의 - 음슴체로 작성할 것. 최대한 간결히 설명하되, 내부 실행에서 어떤 영향을 주는지를  작성할 것.)
        param2: 설명

    Returns:
        반환 설명 (주의 - 음슴체로 작성할 것.)

    Raises:
        예외: 설명 (주의 - 음슴체로 작성할 것.)
    """
```

- `getter`, `setter` 함수에 `get_*` `set_*` 대신 `@property` 를 사용한다.
- 추후 effective python 의 가이드가 이 가이드에 추가될 수 있다.
