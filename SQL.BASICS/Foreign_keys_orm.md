## How Foreign Keys Work in SQLite ORM

Looking at your `Item` class in [`item.py`](LEARNING.SQL.OPERATIONS/n+1./lib/item.py:18-19), you already have the right idea!

### The Concept

A **foreign key** creates a relationship between two tables. In your case:
- `items` table has a `category_id` column
- This `category_id` **references** the `categories` table's `id`
- This establishes: **"An item belongs to ONE category"**

### The SQL in Your Code (Lines 14-21):

```sql
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT,  -- you have INTEGER here, but should be TEXT
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

### Why Use Foreign Keys?

1. **Data Integrity** - Prevents invalid `category_id` values (can't insert an item with a category that doesn't exist)
2. **Relationship Clarity** - Documents that items "belong to" categories
3. **Cascading** - Can set up rules like "if a category is deleted, delete all its items"

### Your ORM Flow:

```
User creates: Item("apple", category_id=1)
    ↓
save() inserts into items table
    ↓
SQL checks: "Does category_id=1 exist in categories table?"
    ↓
If yes → Insert succeeds
If no → Insert fails (foreign key constraint violation)
```

### Note: SQLite Foreign Keys are OFF by default!

You need to enable them with:
```sql
PRAGMA foreign_keys = ON;
```

This is likely why your foreign key isn't enforcing constraints yet—SQLite needs this pragma enabled first.

Does this help clarify the "why" behind foreign keys?