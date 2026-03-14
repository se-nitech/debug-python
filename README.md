# docker composeでpdbを使うサンプルコード

起動

```bash
docker compose build
docker compose up -d
```

実行

```bash
docker compose exec mypython python main.py
```

pdbでデバッグ

```bash
docker compose exec mypython python -m pdb main.py
```

flake8でlint（静的解析）

```bash
docker compose exec mypython flake8 main.py
```

line_profilerでプロファイリング

```bash
docker compose exec mypython kernprof -l main_profile.py
docker compose exec mypython python -m line_profiler main_profile.py.lprof
```

停止

```bash
docker compose stop
docker compose down
```
