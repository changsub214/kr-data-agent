# 데이터 에이전트(Data Agent)

이 프로젝트는 Google ADK(Agent Development Kit)를 사용하여 구축된 데이터 관리, 분석, 시각화 그리고 ML작업이 가능한 에이전트 샘플입니다. 해당 에이전트는 자연어를 통해 BigQuery 내 메타데이터, 데이터 생성과 분석을 진행할 수 있을 뿐만 아니라 모델 생성 및 훈련까지 경험할 수 있습니다. 또한 시각화를 통해 시각화된 결과를 볼 수 있습니다.

## 


## 🚀 기능 (Capabilities)

이 에이전트는 다음과 같은 주요 기능을 수행할 수 있습니다.

* **자연어 쿼리**: 한국어 질문을 이해하여 BigQuery에서 데이터를 조회하고 분석합니다.
* **다양한 차트 생성**: 분석된 데이터를 기반으로 아래와 같은 차트를 동적으로 생성합니다.
    * 막대 차트 (Bar Chart)
    * 선 차트 (Line Chart)
    * 산점도 (Scatter Plot)
    * 히스토그램 (Histogram)
* **이미지 파일 저장**: 생성된 모든 시각화 결과는 서버의 `img/` 디렉터리에 PNG 파일로 저장됩니다.
* **완벽한 한글 지원**: 차트의 제목, 축 라벨 등 모든 한글이 깨짐 없이 정확하게 표시됩니다.

## ✅ 사전 준비 (Prerequisites)

이 에이전트를 실행하기 전에 다음 환경이 준비되어 있어야 합니다.

1.  **Google Cloud Project**: 결제가 활성화된 GCP 프로젝트.
2.  **gcloud CLI**: Google Cloud CLI가 설치 및 인증되어 있어야 합니다.
    * `gcloud auth login`
    * `gcloud auth application-default login`
    * `gcloud auth application-default set-quota-project <YOUR_PROJECT_ID>`
3.  **APIs Enabled**: 프로젝트에서 다음 API가 활성화되어 있어야 합니다.
    * AI Platform API (`aiplatform.googleapis.com`)
    * BigQuery API (`bigquery.googleapis.com`)
4.  **System Fonts**: 에이전트가 실행되는 서버에 **한글 폰트**가 설치되어 있어야 합니다.
    * Ubuntu/Debian 기준: `sudo apt-get update && sudo apt-get install -y fonts-nanum`

## ⚙️ 설치 및 설정 (Setup)

1.  **리포지토리 복제 (Clone Repository)**
    ```bash
    git clone <your-repository-url>
    cd kr-data-agent
    ```

2.  **가상 환경 생성 및 활성화 (Create and Activate Virtual Environment)**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    # For Windows: .\.venv\Scripts\activate
    ```

3.  **의존성 설치 (Install Dependencies)**
    프로젝트 루트의 `pyproject.toml` 파일을 사용하여 모든 필수 라이브러리를 설치합니다.
    ```bash
    pip install .
    ```

4.  **환경 변수 설정 (Configure Environment Variables)**
    프로젝트 루트에 `.env` 파일을 생성하고 아래 내용을 채워넣습니다.
    ```env
    # .env
    MODEL="gemini-1.5-pro-preview-0409"
    GCP_PROJECT_ID="your-gcp-project-id"
    ```

## 🏃 실행 방법 (How to Run)

아래 명령어를 사용하여 로컬 ADK 웹 서버를 시작합니다.
서버가 시작되면 http://127.0.0.1:8000 주소로 접속하여 웹 UI에서 에이전트와 상호작용할 수 있습니다. 생성된 차트 이미지는 kr_bq_agent/sub_agents/visualization_agent/img/ 디렉터리에 저장됩니다.

🗣️ 샘플 프롬프트 (Sample Prompts)
에이전트에게 다음과 같은 질문을 할 수 있습니다.

bank 데이터세트 내 customer_id 테이블 참고해서 성별별 가입자수를 막대 차트로 나타내줘

지난 한 해 동안의 월별 매출 추이를 선 차트로 보여줘

광고비와 매출 사이의 상관관계를 산점도로 시각화해줘

사용자 연령 분포를 히스토그램으로 그려줘
