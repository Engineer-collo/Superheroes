# Superheroes API

## Project Description
This project is an API for tracking heroes and their superpowers using Flask and SQLAlchemy. It enables users to retrieve information about heroes, powers, and their associations, as well as create and update relevant data.

## Setup Instructions

### 1. Repository Setup
- Create a **private repository** on GitHub.
- Add your **Technical Mentor (TM)** as a collaborator.
- Push your solution to this repository and submit it for grading.

### 2. Postman Collection
A Postman collection is provided to test the API endpoints.

#### How to Import Postman Collection:
1. Open **Postman**.
2. Select **Import**.
3. Choose **Upload Files**.
4. Navigate to the repository folder and select `challenge-2-superheroes.postman_collection.json`.
5. Click **Import**.

### 3. Running the Application
1. Clone the repository:
   ```sh
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run database migrations and seed data:
   ```sh
   flask db upgrade
   flask seed run  # If provided, or create your own seed data
   ```
5. Start the server:
   ```sh
   flask run
   ```

## Data Models
### Hero
- `id`: Integer (Primary Key)
- `name`: String
- `super_name`: String
- **Relationships**: Has many `Power`s through `HeroPower`.

### Power
- `id`: Integer (Primary Key)
- `name`: String
- `description`: String (Must be at least **20 characters long**).
- **Relationships**: Has many `Hero`s through `HeroPower`.

### HeroPower
- `id`: Integer (Primary Key)
- `hero_id`: Foreign Key (References `Hero`)
- `power_id`: Foreign Key (References `Power`)
- `strength`: String (Must be **Strong, Weak, or Average**).
- **Relationships**: Belongs to a `Hero` and a `Power`.

## API Endpoints

### 1. GET /heroes
**Response:**
```json
[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl" }
]
```

### 2. GET /heroes/:id
**Response (Success):**
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```
**Response (Not Found):**
```json
{
  "error": "Hero not found"
}
```

### 3. GET /powers
**Response:**
```json
[
  { "id": 1, "name": "super strength", "description": "gives the wielder super-human strengths" },
  { "id": 2, "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" }
]
```

### 4. GET /powers/:id
**Response (Success):**
```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```
**Response (Not Found):**
```json
{
  "error": "Power not found"
}
```

### 5. PATCH /powers/:id
**Request:**
```json
{
  "description": "Valid Updated Description"
}
```
**Response (Success):**
```json
{
  "id": 1,
  "name": "super strength",
  "description": "Valid Updated Description"
}
```
**Response (Not Found):**
```json
{
  "error": "Power not found"
}
```
**Response (Validation Error):**
```json
{
  "errors": ["validation errors"]
}
```

### 6. POST /hero_powers
**Request:**
```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```
**Response (Success):**
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
```
**Response (Validation Error):**
```json
{
  "errors": ["validation errors"]
}
```

## Validations
- `strength` in `HeroPower` **must be**: `Strong`, `Weak`, or `Average`.
- `description` in `Power` **must be at least** 20 characters long.

## Submission Checklist
✔ Push your code to a **private GitHub repository**.  
✔ Add your **TM as a collaborator**.  
✔ Ensure all **routes work as expected**.  
✔ Verify that your **README is well-formatted** using VS Code Markdown Preview.  
✔ Submit your repository link for grading.  

**Author:** Collins Likhomba.



