from fastapi import FastAPI

from app.api.routes import expense, group, settlement, user

app = FastAPI(title="ExpenseHub")
app.include_router(user.router)
app.include_router(group.router)
app.include_router(expense.router)
app.include_router(settlement.router)


@app.get("/health")
def health():
   return {"status": "ok"}
