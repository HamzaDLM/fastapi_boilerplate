# **FastAPI Boilerplate**

### **Description**
This FastAPI boilerplate covers most important features like testing, db integration, job queueing with celery, docker integration and api versionning, it also comes with a pre-configured custome loghandler to view your logs from an HTML page or download them.

### **Run Project**
After cloning the boilerplate, navigate to folder and use command:
```bash
uvicorn main:app --reload
```
or using docker
```bash
docker-compose build
docker-compose up
```

### **API documentation:**
Documentations for all APIs are auto-generated using FastAPI's Swagger UI
<http://127.0.0.1:8004/docs#/>

### **Folder Structure**
    .                        
    ├── main.py                 # Runtime
    ├── utils.py                # Contains logic
    ├── worker.py               # Celery tasks
    ├── schemas                 # Request and Reponse Schemas
    ├── models                  # ORM mapping
    ├── .env                    # environment variables
    ├── db            
    |   └── session.py          # MySQL session
    ├── core            
    |   └── config.py           # configuration parameters
    └── api          
        ├── deps.py             # dependencies
        └── api_v1          
            ├── api.py          # API routers    
            └── endpoints       
                ├── endpoint1   # API endpoint
                └── endpoint2   # API endpoint
                  
            
