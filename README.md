# 데이터 에이전트(Data Agent)

이 프로젝트는 Google ADK(Agent Development Kit)를 사용하여 구축된 데이터 관리, 분석, 시각화 그리고 ML작업이 가능한 에이전트 샘플입니다. 해당 에이전트는 자연어를 통해 BigQuery 내 메타데이터, 데이터 생성과 분석을 진행할 수 있을 뿐만 아니라 모델 생성 및 훈련까지 경험할 수 있습니다. 또한 시각화를 통해 시각화된 결과를 볼 수 있습니다.

## 📃 구조 (Architecture)
```bash
KR_BQ_AGENT/
├── sub_agents/
│   ├── bqml_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompts.py
│   ├── data_analytics_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompts.py
│   ├── data_management_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompts.py
│   ├── visualization_agent/
│   │   ├── img/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── tools.py
│   ├── __init__.py
│   └── .env.example
├── __init__.py
├── .env.example
├── agent.py
├── prompts.py
└── pyproject.toml
```

## 🚀 기능 (Capabilities)

이 에이전트는 다음과 같은 주요 기능을 수행할 수 있습니다.

* **자연어 쿼리**: 질문을 이해하여 BigQuery에서 데이터를 조회하고 분석합니다.
* **메타데이터 및 데이터 관리**: 스키마와 데이터를 이해하여 적절한 메타데이터 생성뿐만 아니라 데이터 관리가 가능합니다.
* **모델 생성 및 훈련**: BigQueryML에서 지원하는 머신러닝 모델을 생성하고 데이터 훈련이 가능합니다. 
* **시각화 생성**: 분석된 데이터를 기반으로 아래와 같은 차트를 동적으로 생성합니다.
    * 막대 차트 (Bar Chart)
    * 선 차트 (Line Chart)
    * 산점도 (Scatter Plot)
    * 히스토그램 (Histogram)

## ✅ 사전 준비 (Prerequisites)

이 에이전트를 실행하기 전에 다음 환경이 준비되어 있어야 합니다.

1.  **Google Cloud Project**: 결제가 활성화된 GCP 프로젝트.
2.  **gcloud CLI**: Google Cloud CLI가 설치 및 인증되어 있어야 합니다.
    * <a href="https://cloud.google.com/sdk/docs/install?hl=ko" target="_blank">설치링크</a>
    * `gcloud auth login`
    * `gcloud auth application-default login`
    * `gcloud auth application-default set-quota-project <YOUR_PROJECT_ID>`
4.  **APIs Enabled**: 프로젝트에서 다음 API가 활성화되어 있어야 합니다. 구글 클라우드 콘솔에서 다음 API 검색하여 활성화 확인합니다.
    * Vertex AI API
    * BigQuery API
5.  **Python version**: Python 3.12+ 이상이어야 합니다.
6.  **Git**: git이 설치되어 있어야 합니다.
    * <a href="https://git-scm.com/" target="_blank">설치링크</a>
    * <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" target="_blank">가이드라인</a>
7.  **IAM**: 연결된 계정이 최소한 BigQuery Editor, Vertex AI User 권한 이상을 가져야 합니다.
8.  **[Optional]System Fonts**: 에이전트가 실행되는 환경에 **나눔고딕 폰트**가 설치되어 있어야 합니다.
    * Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y fonts-nanum`
    

## ⚙️ 설치 및 설정 (Setup)

1.  **리포지토리 복제 (Clone Repository)**
    ```bash
    git clone https://github.com/changsub214/kr-data-agent.git
    cd kr-data-agent
    ```

2.  **가상 환경 생성 및 활성화 (Create and Activate Virtual Environment)**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **의존성 설치 (Install Dependencies)**
    kr_bq_agent 폴더로 이동 후 `pyproject.toml` 파일을 사용하여 모든 필수 라이브러리를 설치합니다. 이후 상위 디렉터리로 이동합니다.
    ```bash
    cd kr_bq_agent
    pip install .
    cd ..
    ```

4.  **환경 변수 설정 (Configure Environment Variables)**
    kr_bq_agent 내 루트와 sub_agents/에 `.env.example` 파일을 `.env`로 수정하고 양식에 맞춰 값을 채워넣습니다.
    ```env
    GOOGLE_GENAI_USE_VERTEXAI=TRUE
    #GOOGLE_API_KEY="" #If you want to use API, you should set this value and FALSE on upper value and then you can use it.
    GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    GOOGLE_CLOUD_LOCATION="YOUR_REGION"
    MODEL = "YOUR MODEL"
    ```

## 🏃 실행 방법 (How to Run)

아래 명령어를 사용하여 로컬 ADK 웹 환경을 시작합니다. 이때 위치는, kr-data-agent/ 에 위치해야 합니다.
```bash
adk web
```
시작되면 http://127.0.0.1:8000 주소로 접속하여 웹 UI에서 에이전트와 상호작용할 수 있습니다. 생성된 차트 이미지는 kr_bq_agent/sub_agents/visualization_agent/img/ 디렉터리에 저장됩니다.
만일, CLI 환경에서 진행할 경우 다음과 같이 진행합니다.
```bash
adk run kr_bq_agent
```

## 🗣️ 샘플 프롬프트 (Sample Prompts)
에이전트에게 다음과 같은 질문을 할 수 있습니다.

은행 관련 고객 정보가 있는 테이블에서 성별별 가입자수를 나타내줘

지난 한 해 동안의 월별 매출 추이를 보여줘

광고비와 매출 사이의 상관관계를 분석하고 산점도로 시각화해줘

인구관련 데이터세트에서 인사이트를 얻기 위한 적절한 질문 3개 생성해줘

코흐트 분석해줘

인구 변화 예측을 하고 싶은데 적절한 모델 생성하고 평가해줘

고객 테이블 메타데이터 생성해줘
