# Magic Pinecone Backend 🌲

> **備註**: 本 README 文件由 **Gemini** 生成。

歡迎來到 **Magic Pinecone Backend**！這是一個基於 **FastAPI**、**SQLAlchemy** 與 **PostgreSQL** 建構的後端 API 服務專案。旨在讓中央大學（NCU）的學生能夠在單一平台上輕鬆獲取並整合校園內龐大的資訊。

## 🚀 核心特色

- **FastAPI 驅動**: 提供現代化、高效能的 Python 網頁框架設計。
- **PostgreSQL 資料庫**: 支援關聯式資料庫，用於管理課程、系所與學院等模型。
- **Docker 容器化**: 透過 `docker-compose` 包含應用程式、資料庫與 Digirunner，輕鬆完成基礎設施配置與部署。
- **課程資料爬取 (Course Finder Fetching)**: 內建自動 / 手動向學校系統同步最新課程資料的功能。
- **排程功能**: 透過 `APScheduler` 自動處理背景定時任務。

---

## 📚 Course Finder Fetching (課程資料爬取與同步)

本後端的重點功能之一，是能將 NCU 校務系統的課程資料抓取下來並解析，將資料同步存入本地的 PostgreSQL 資料庫中，以實現快速的查詢與讀取。

**運作機制：**
爬蟲程式藉由 `httpx` 向學校的課程系統取得各學院與系所的資料（包含解析 XML 格式的課程細節及藉由 `BeautifulSoup` 抓取 HTML 頁面的課程屬性），隨後將最新資訊以批次的方式合併並更新 (UPSERT) 到資料庫中。

**觸發同步的方式：**
1. **排程自動更新**: 推出的 FastAPI 生命週期事件中整合了 `APScheduler`，預設為 **每日凌晨 04:00** 自動在背景觸發一次課程資料爬取與同步。
2. **手動 API 觸發**: 若需即時更新，可向 `/course/sync` 路由發送 `POST` 請求。這將利用 FastAPI 的 `BackgroundTasks` 在背景啟動課程同步程序，無需等待爬蟲執行完畢即可獲得 API 響應。

---

## 🛠️ 開始使用

### 環境需求

- [Docker](https://docs.docker.com/engine/install/) & [Docker Compose](https://docs.docker.com/compose/install/)
- (可選) 本機開發可使用 [uv](https://github.com/astral-sh/uv) (本專案依賴需要 Python 3.13+)

### 使用 Docker 快速啟動（建議）

使用 Docker Compose 是最簡單的啟動方式，它將預設啟動您的 Backend API、PostgreSQL 資料庫與 Digirunner Gateway。

1. **環境變數設定**:
   複製範例環境變數檔，並根據您的需求進行修改。
   ```bash
   cp example.env .env
   ```

2. **啟動所有服務**:
   ```bash
   docker-compose up -d --build
   ```

3. **存取服務**:
   - Backend API 主機: `http://localhost:8000`
   - FastAPI (Swagger) 文件: `http://localhost:8000/docs`
   - Digirunner Gateway: `http://localhost:18080`

### 本機開發設定 (不使用 Docker)

若您想在自己的電腦開發環境中直接執行除錯：

1. 建立環境與安裝相依套件 (由 `pyproject.toml` 或 `uv.lock` 管理)。
   ```bash
   uv sync
   ```
2. 準備本機的 PostgreSQL 資料庫，並在 `.env` 中設定對應的 DB 連線環境變數（如 `DB_USER`、`DB_PASSWORD` 及 `DB_NAME`）。
3. 透過 Uvicorn 啟動 FastAPI 開發伺服器。
   ```bash
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 🏆 致謝 (Acknowledgments)

特別感謝以下專案為本後端的課程爬蟲功能提供實作靈感與參考：

- **Course Finder Fetcher**: [NCU-Course-Finder-DataFetcher-v2](https://github.com/zetaraku/NCU-Course-Finder-DataFetcher-v2)
