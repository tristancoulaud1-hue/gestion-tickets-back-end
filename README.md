# 🎫 Ticket Manager — Backend (FastAPI)

Prototype d’API REST pour centraliser et suivre des demandes (tickets) **sans base de données** : les données sont stockées dans un fichier JSON.

## ✅ Fonctionnalités

- CRUD tickets : **GET / POST / PATCH / DELETE**
- Validation stricte avec **Pydantic**
- Filtres : `status`, `priority`, `tag`, `search`, `fromDate`, `toDate`
- Tri : `sortBy` + ordre `order=asc|desc`
- Pagination : `page`, `limit`
- Gestion d’erreurs HTTP (400 / 404 / 422)

---

## 🧱 Structure

Exemple (peut varier selon ton repo) :

```
backend/
├── main.py
├── routes/
│   └── tickets.py
├── services/
│   └── ticket_service.py
├── models/
│   └── ticket.py
└── data/
    └── tickets.json
```

---

## ⚙️ Prérequis

- Python 3.10+
- pip
- (optionnel) venv

---

## 🚀 Installation

### 1) Créer un environnement virtuel

Depuis la racine du projet :

```bash
python -m venv venv
```

Activation :

**Windows (PowerShell)**

```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bat
venv\Scripts\activate.bat
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 2) Installer les dépendances

```bash
pip install fastapi uvicorn
```

> Optionnel :

```bash
pip install "uvicorn[standard]"
```

---

## ▶️ Lancer l’API

Depuis la racine du projet :

```bash
uvicorn backend.main:app --reload
```

- API : http://127.0.0.1:8000
- Swagger : http://127.0.0.1:8000/docs

---

## 🗂️ Données (JSON)

Le stockage est fait dans :

```
backend/data/tickets.json
```

Chaque ticket ressemble à :

```json
{
  "id": 1,
  "title": "Bug bouton login",
  "description": "Le bouton de connexion ne répond pas sur mobile (Android).",
  "priority": "High",
  "status": "Open",
  "tags": ["bug", "ui", "mobile"],
  "createdAt": "2026-01-16"
}
```

---

## 🔒 Validation (Pydantic)

### Status autorisés

- `Open`
- `In Progress`
- `Done`

### Priority autorisées

- `Low`
- `Medium`
- `High`

⚠️ Attention : validation **stricte** (casse/espaces exacts).  
Ex: `In Progress` ✅ mais `In progress` ❌ (422)

---

## 📌 Endpoints

### ✅ GET `/tickets`

Récupère les tickets (avec filtres/tri/pagination).

**Query params**

- `status` : `Open | In Progress | Done`
- `priority` : `Low | Medium | High`
- `tag` : ex `bug`
- `search` : recherche texte (title + description)
- `fromDate` : `YYYY-MM-DD`
- `toDate` : `YYYY-MM-DD`
- `sortBy` : `createdAt | title | priority` (ou autre champ existant)
- `order` : `asc | desc` (par défaut `asc`)
- `page` : entier (défaut `1`)
- `limit` : entier (défaut `5`)

**Exemples**

```bash
# Simple
curl "http://127.0.0.1:8000/tickets"

# Filtres
curl "http://127.0.0.1:8000/tickets?status=Open&priority=High"

# Tag + search
curl "http://127.0.0.1:8000/tickets?tag=bug&search=mobile"

# Tri + ordre
curl "http://127.0.0.1:8000/tickets?sortBy=createdAt&order=desc"

# Pagination
curl "http://127.0.0.1:8000/tickets?page=2&limit=5"
```

**Réponse (pagination)**

```json
{
  "page": 1,
  "limit": 5,
  "total": 10,
  "pages": 2,
  "data": [ ... ]
}
```

---

### ✅ POST `/tickets`

Crée un ticket.

```bash
curl -X POST "http://127.0.0.1:8000/tickets" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Problème notification",
    "description": "Envoyer un email automatique au créateur du ticket.",
    "priority": "Medium",
    "status": "Open",
    "tags": ["feature", "notification"],
    "createdAt": "2026-01-18"
  }'
```

---

### ✅ PATCH `/tickets/{id}`

Met à jour un ticket (champs partiels acceptés).

```bash
curl -X PATCH "http://127.0.0.1:8000/tickets/1" \
  -H "Content-Type: application/json" \
  -d '{ "status": "In Progress" }'
```

> Si `id` n’existe pas → `404 Ticket not found`

---

### ✅ DELETE `/tickets/{id}`

Supprime un ticket.

```bash
curl -X DELETE "http://127.0.0.1:8000/tickets/1"
```

---

## 🧯 Codes d’erreur

- `400 Bad Request` : paramètre invalide (ex: `sortBy` incorrect)
- `404 Not Found` : ticket introuvable
- `422 Unprocessable Entity` : validation Pydantic échoue (format/casse/valeurs)

---

## 🧪 Tests rapides (manuel)

1. Lancer l’API
2. Ouvrir Swagger : http://127.0.0.1:8000/docs
3. Tester :
   - POST (création)
   - GET (liste + filtres)
   - PATCH (statut)
   - DELETE

---

## 🧩 Notes techniques

- Stockage JSON : simple, rapide, idéal pour prototype
- IDs générés automatiquement côté backend
- Architecture en couches (routes/services/models) pour se rapprocher des pratiques entreprise
