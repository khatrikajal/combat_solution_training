FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV STREAMLIT_DISABLE_BROWSER=true

CMD ["streamlit", "run", "langgraph/azureopenai_langgraph.py", "--server.address=0.0.0.0", "--server.port=8501"]
