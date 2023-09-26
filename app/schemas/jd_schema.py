from pydantic import BaseModel

# Rating model


class RatingBase(BaseModel):
    RAW_ID: int
    PRODUCT_SIN: str
    goodRateShow: str
    score1Count: str
    score2Count: str
    score3Count: str
    score4Count: str
    score5Count: str
    SCRAPY_DT_STR: str
    SITE_ID: str


class RatingCreate(RatingBase):
    pass


class Rating(RatingBase):
    class Config:
        orm_mode = True

# Review model


class ReviewBase(BaseModel):
    PRODUCT_SIN: str
    SITE_REVIEW_ID: str
    SITE_REVIEW_URL: str
    SITE_REVIEW_DATE_STR: str
    SITE_REVIEW_TITLE: str
    SITE_REVIEW_MESSAGE_HTML: str
    SITE_REVIEW_MESSAGE: str
    SITE_REVIEW_RATING: str
    SCRAPY_DT_STR: str
    USER_NAME: str
    RATING: str
    REVIEW_DATE: datetime
    AFTER_REVIEW_MESSAGE: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    class Config:
        orm_mode = True

# Items model

class ItemsBase(BaseModel):
    SKU_ID: str
    SITE_ID: str
    COLLECT_STATUS: str


class ItemsCreate(ItemsBase):
    pass


class Items(ItemsBase):
    class Config:
        orm_mode = True


class ReviewIdBase(BaseModel):
    SITE_ID: str
    SITE_REVIEW_ID: str


class ReviewIdCreate(ReviewIdBase):
    pass


class ReviewId(ReviewIdBase):
    class Config:
        orm_mode = True
