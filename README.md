Python for Data Engineering Roadmap
Progress tracker for learning Python from beginner to advanced, focused on data engineering.
Progress: 2/33 topics (0%)

Phase 1 — Python Foundations
- [X] Variables, data types & operators — int, float, str, bool, list, dict, tuple, set
- [X] Control flow — if/elif/else, for & while loops, break/continue
- [X] Functions — def, return, *args, **kwargs, default parameters
- [X] List & dict comprehensions — Compact data transformation in one line
- [X] String methods & f-strings — split, strip, join, format strings
- [ ] Error handling — try/except/finally, raising custom exceptions
- [ ] Modules, packages & venv — import, pip install, requirements.txt

Phase 2 — Data Handling with pandas
- [ ] File I/O — open(), read(), write(), context managers (with)
- [ ] CSV & JSON processing — csv module, json module, nested data parsing
- [ ] pandas basics — DataFrame, read_csv, head, info, dtypes
- [ ] pandas transformations — groupby, agg, merge, pivot_table, apply
- [ ] pandas cleaning — dropna, fillna, astype, drop_duplicates
- [ ] datetime & timedelta — Parsing dates, timezones, strftime/strptime
- [ ] Working with REST APIs — requests library, GET/POST, JSON responses

Phase 3 — Database Integration
- [ ] psycopg2 basics — Connect to PostgreSQL, execute, fetchall, commit
- [ ] SQLAlchemy Core — Engine, connections, raw queries with text()
- [ ] SQLAlchemy ORM — Models, sessions, relationships
- [ ] pandas to/from SQL — read_sql() and to_sql() for DataFrame <-> DB
- [ ] Schema management — CREATE TABLE, IF NOT EXISTS, basic migrations
- [ ] Environment & credentials — python-dotenv, .env files, secure config

Phase 4 — ETL Pipeline Building
- [ ] Extract patterns — API pagination, rate limits, retry logic
- [ ] Data validation — Schema checks, type coercion, pydantic basics
- [ ] Transform patterns — Flatten nested JSON, normalize, type casting
- [ ] Load patterns — Incremental loading, upsert (ON CONFLICT), watermarking
- [ ] Logging — logging module, log levels, writing logs to file
- [ ] Scheduling basics — APScheduler, cron syntax

Phase 5 — Apache Airflow Orchestration
- [ ] DAG structure — DAG, schedule_interval, start_date, catchup
- [ ] Operators — PythonOperator, BashOperator, PostgresOperator
- [ ] Task dependencies — >> and << operators, set_upstream/downstream
- [ ] XCom — Passing data between tasks with xcom_push/xcom_pull
- [ ] Connections & Variables — Managing config via Airflow UI
- [ ] Error handling & retries — retries, retry_delay, on_failure_callback

Phase 6 — Engineering Best Practices
- [ ] Project structure — src/, tests/, config/, dags/, utils/ layout
- [ ] Testing with pytest — assert, fixtures, mocking DB/API calls
- [ ] Type hints — Optional, List, Dict annotations for cleaner code
- [ ] Git workflow for DE projects — .gitignore for secrets & data files
