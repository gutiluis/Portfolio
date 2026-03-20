-- 3 ways to run the query:
-- python,
-- psql from docker connecting to supabase,
-- supabase cli
SELECT relname AS table_name,
       relrowsecurity AS rls_enabled
FROM pg_class
WHERE relname = 'projects';
-- return true when active
-- return false when inactive