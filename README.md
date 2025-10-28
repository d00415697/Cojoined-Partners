# **Predator Message Log**

## **Resource**
**Message**

### **Attributes**
- `name` (string) — Predator’s name  
- `description` (string) — Short description of the Predator  
- `age` (integer) — Predator’s age  
- `rank` (string) — Predator’s Yautja ranking  
- `kills` (integer) — Number of confirmed kills  

---

## **Schema**

```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    age INTEGER,
    rank TEXT,
    kills INTEGER
);
```

## **REST Endpoints**

| **Name** | **Method** | **Path** | **Description** |
|-----------|-------------|----------|------------------|
| Retrieve message collection | GET | `/messages` | Returns all Predator records as JSON |
| Retrieve single message | GET | `/messages/<id>` | Returns a single Predator record by ID *(optional)* |
| Create message | POST | `/messages` | Adds a new Predator record |
| Update message | PUT | `/messages/<id>` | Updates an existing Predator record |
| Delete message | DELETE | `/messages/<id>` | Deletes a Predator record by ID |
