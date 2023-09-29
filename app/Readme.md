# 專案架構參考
https://camillovisini.com/article/abstracting-fastapi-services/




# 目標

練習使用FastAPI建立一個結合MYSQL DB的API server，將依照以下功能規劃進行開發。

## 專案相關功能規劃

1. * 路徑: /v1/items
   * 功能: 回傳資料庫中所有產品ID
   * Method: "GET"
   * Status code: 200
___________________________
2. * 路徑: /v1/item/{sku_id}
   * 功能: 取得單一產品下所有評論
   * Method: "GET"
   * Status code: 200
___________________________
3. * 路徑: /v1/add_item
   * 功能: 新增產品
   * Method: "POST" or "PUT"
   * Status code: 200
___________________________
4. * 路徑: /v1/item/{sku_id}
   * 功能: 更新產品資訊
   * Method: "PUT"
   * Status code: 200
___________________________
5. * 路徑: /v1/item/{sku_id}
   * 功能: 刪除指定產品
   * Method: "DELETE" or "PUT" (軟刪除設定)
   * Status code: 200
___________________________
## 評論相關功能規劃

1. * 路徑: /v1/reviews
   * 功能: 回傳所有產品評論
   * Method: "GET"
   * Status code: 200
___________________________
2. * 路徑: /v1/review/{review_id}
   * 功能: 回傳特定產品評論
   * Method: "GET"
   * Status code: 200
___________________________
## 評價相關功能規劃

1. * 路徑: /v1/ratings
   * 功能: 回傳所有產品最新評價
   * Method: "GET"
   * Status code: 200
