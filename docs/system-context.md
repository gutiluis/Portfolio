           ┌───────────────┐
           │     User      │
           │   (Browser)   │
           └───────┬───────┘
                   │
                   │ HTTPS
                   ▼
        ┌─────────────────────┐
        │   Cloudflare Pages  │
        │  Frontend Hosting   │
        └─────────┬───────────┘
                  │
                  │ API Requests (fetch)
                  ▼
        ┌─────────────────────┐
        │      Supabase       │
        │  Backend-as-a-Service │
        │  REST API + Auth    │
        └─────────┬───────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │ PostgreSQL Database │
        │   (Supabase DB)     │
        └─────────────────────┘
