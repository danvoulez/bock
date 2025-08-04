create table if not exists chat_sessions (
  id uuid primary key default uuid_generate_v4(),
  title text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

alter table chat_sessions enable row level security;