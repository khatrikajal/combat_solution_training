# Combat Solution Training – Azure OpenAI + LangChain + LangGraph + Docker + DAG

##  Project Structure
```
combat_solution_training/
│
├── azure_openapi/      # Task 1: Azure OpenAI basics & API integration
│   ├── .env
│   ├── call_azureOpenAPI.py
│
├── langchain/          # Task 2: LangChain basics
│   ├── .env
│   ├── langchain_model.py
│
├── langgraph/          # Task 3: LangGraph chatbot workflow with azureopen ai
│   ├── .env
│   ├── azureopenai_langgraph.py
│
├── dag/                # Task 5: DAG implementation with LangGraph
│   ├── ...
│
├── Dockerfile          # Task 4: Containerization langgraph only 
├── docker-compose.yml
├── requirements.txt
└── README.md           
```

---

## Task Details

### **Task 1 – Learn Azure OpenAI Basics**  
**Folder:** `azure_openapi/`  
**Objectives:**
- Understand Azure OpenAI vs OpenAI.com
- Access models via Azure portal
- Learn LLM concepts: tokens, prompts, completions
- Create Azure OpenAI resource in Azure Portal
- Configure API key & endpoint in `.env`

**Deliverables:**
- Azure OpenAI resource created
- Playground prompt tested
- `call_azureOpenAPI.py` to call Azure GPT-3.5 API using key & endpoint

---

### **Task 2 – Learn LangChain Basics**  
**Folder:** `langchain/`  
**Objectives:**
- Learn LangChain concepts: LLMs, Chains, Memory, Tools
- Build a simple LangChain:
  - PromptTemplate
  - ChatOpenAI model
  - ConversationBufferMemory

**Deliverables:**
- LangChain script connecting prompt, LLM, and memory
- Tested with openrouter "mistralai/mistral-7b-instruct:free" model

---

### **Task 3 – Build a Simple LangGraph Flow**  
**Folder:** `langgraph/`  
**Objectives:**
- Learn LangGraph concepts: Graph, Nodes, Edges, State Management
- Build a minimal chatbot:
  1. Input Node → LLM Node (Azure GPT-3.5) → Memory Node → Output Node

**Deliverables:**
- `azureopenai_langgraph.py` with working chatbot flow

---

### **Task 4 – Dockerize the LangGraph Chatbot**  
**Folder:** `langgraph/` (Docker runs from here)  
**Objectives:**
- Understand Docker basics: Image vs Container, Dockerfile, Docker Compose
- Create a containerized environment for LangGraph chatbot

**Deliverables:**
- `Dockerfile` & `docker-compose.yml`
- Runs chatbot in container with:
  ```bash
  docker-compose up --build
  ```
- Exposes chatbot at [http://localhost:8501](http://localhost:8501)

---

### **Task 5 – DAG Implementation in LangGraph**  
**Folder:** `dag/`  
**Objectives:**
- Understand Directed Acyclic Graph (DAG) in LangGraph
- Implement branching workflow:
  - If input is calculation → route to tool node
  - If input is text → route to LLM node

**Deliverables:**
- Multi-path DAG script with decision-based routing
- No cycles; clean input-to-output flow

---

## Environment Variables
Each task folder contains its own `.env` file:
```env
ENDPOINT_URL=https://<your-resource-name>.openai.azure.com/
DEPLOYMENT_NAME=gpt-35-turbo
AZURE_OPENAI_API_KEY=<your-api-key>
```

---

##  How to Run
### Local (Python)
```bash
pip install -r requirements.txt

# for azure_apenai
python azureOpenai_call.py

# for langchain
cd langchain
streamlit run langchain_model.py

# for dag 
cd dag
streamlit run app.py


```

### Docker
```bash
# for langgraph

docker-compose up --build
```
Visit: [http://localhost:8501](http://localhost:8501)

---

##  Learning Goals
- **Azure OpenAI**: Deploy & call GPT models from Azure portal  
- **LangChain**: Build LLM chains with memory  
- **LangGraph**: Create multi-node conversational flows  
- **Docker**: Package chatbot for consistent deployment  
- **DAG**: Build decision-based AI workflows  
