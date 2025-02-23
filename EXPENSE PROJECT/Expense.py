import uuid
from datetime import datetime, timezone

class Expense:
    # Initializes the attributes.
    def __init__ (self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        
    # Allows updating the title and/or amount, updating the updated_at timestamp.
    def update (self, title = None, amount = None):
        if title is not None:
            self.title = str(title)
        if amount is not None:
            self.amount = float(amount)
        self.updated_at = datetime.now(timezone.utc)
        
    #Returns a dictionary representation of the expense.
    def to_dict (self):
        return{
            "Expense_id": self.id,
            "Title": self.title,
            "Amount": self.amount,
            "Created_time": self.created_at.isoformat(),
            "Updated_time": self.updated_at.isoformat()
        }
    

expense1 = Expense("Food", 400.50)

print(expense1.to_dict())

expense1.update (amount = 670.67)
print( expense1.to_dict())


class ExpenseDB:
    def __init__ (self):
        self.expense = []
    
    #Add an expense to the database.
    def add_expense (self, expense):
        self.expense.append(expense)
    
    #Remove an expense from the database using ID.
    def remove_expense_id (self, expense_id):
        self.expense = [ex for ex in self.expense if ex.id != expense_id]
    
    #Remove an expense from the database using name.
    def remove_expense_name (self, expense_title):
        self.expense = [ex for ex in self.expense if ex.title != expense_title]
        
    # Get an expense by ID.
    def get_expense_id (self, expense_id):
        for ex in self.expense:
            if ex.id == expense_id:
                return [ex.to_dict() for ex in self.expense]
        
    def get_expense_name (self, expense_title):
        for ex in self.expense: 
            if ex.title == expense_title:
                return ex.to_dict()
        return None
    
    def to_dict (self):
        return[ex.to_dict() for ex in self.expense]
    

# Create new expenses
expense2 = Expense("Coffee", 3.50)
expense3 = Expense("Lunch", 12.00)

print (expense3.to_dict())

DB = ExpenseDB()

DB.add_expense(expense2)
DB.add_expense(expense1)
DB.add_expense(expense3)

print(f"List of Expense to: {DB.get_expense_name('Coffee')}")


print(f"List of Expenses: {DB.to_dict()}")




