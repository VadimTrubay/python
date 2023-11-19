from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    name: str = Field(max_length=100)
    price: str = Field(max_length=5)


class ProductResponse(ProductModel):
    id: int

    class Config:
        orm_mode = True













