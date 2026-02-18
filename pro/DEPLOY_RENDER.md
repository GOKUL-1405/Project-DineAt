# Deploying Project-DineAt to Render

This document explains how to connect the repository to Render and run the first deploy. I added `render.yaml` and a GitHub Action to run `collectstatic` and `migrate` on pushes to `main`.

1) Connect the repo in Render

- Sign in to https://render.com and choose "New+" → "Web Service".
- Select "Repository" and connect your GitHub account, then choose the repository: `GOKUL-1405/Project-DineAt` and branch `main`.
- Render will detect `render.yaml` and propose a service named `dineat-web`. If it doesn't, create a Python web service and use these values:
  - Build Command: `pip install -r pro/backend/requirements.txt`
  - Start Command: `gunicorn DineAt.wsgi:application --chdir pro/backend --bind 0.0.0.0:$PORT`

2) Environment variables / Secrets

Set these environment variables in the Render service settings (or use the dashboard UI):

- `SECRET_KEY` — set a secure value
- `DEBUG` — `false`
- `ALLOWED_HOSTS` — your domain or `*` for testing
- `GEMINI_API_KEY` — (optional) if you use Gemini

If you prefer Render's managed Postgres (recommended): create a database service in Render and copy its connection string into:

- `DATABASE_URL` — e.g. `postgres://USER:PASS@HOST:PORT/NAME`

3) Run initial database migrations and collectstatic

You can run these from the Render dashboard Console for the deployed service or rely on the GitHub Action added to the repo.

From the Render Console (or an SSH shell attached to the service):

```bash
python pro/backend/manage.py migrate --noinput
python pro/backend/manage.py collectstatic --noinput
```

4) GitHub Actions and repository secrets

The repo includes a workflow at `pro/.github/workflows/migrate-and-collectstatic.yml` that runs `collectstatic` and `migrate` on pushes to `main`.
Add these Secrets in your GitHub repository settings → Secrets:

- `SECRET_KEY` — same value as in Render
- `DATABASE_URL` — connection string for the DB Render can access

5) Post-deploy checks

- Visit the Render service URL (or your custom domain) to verify pages load.
- Check the logs in Render if the app fails to start (common issues: missing env vars, DB connectivity, static files not collected).

6) Useful local commands

```bash
# run the Django dev server from repository root
python pro/backend/manage.py runserver

# run migrations locally
python pro/backend/manage.py migrate

# collect static files locally
python pro/backend/manage.py collectstatic --noinput
```

7) Notes & recommendations

- `settings.py` now includes WhiteNoise and `STATICFILES_STORAGE` so static files will be served in production.
- The repo previously had `pro/backend` as a gitlink; it is now included in the main repo.
- Use a managed Postgres database for production instead of the default MySQL or SQLite.

If you'd like, I can guide you step-by-step through the Render UI while you connect the repo, or I can create a `render.yaml` variant for MySQL. Which would you like next?
