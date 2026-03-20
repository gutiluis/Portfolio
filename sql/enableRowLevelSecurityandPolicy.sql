-- not used because users dont need to login. there wont be users...
-- Enable Row Level Security. fix public
ALTER TABLE projects ENABLE ROW LEVEL SECURITY; -- from supabase docs

-- Create RLS policies
-- Once you have enabled RLS, no data will be accessible via the API...
-- when using the public anon key, until you create policies.

-- What auth.uid() is
-- auth.uid() in RLS policies returns the UUID of the currently authenticated user.
-- If no user is logged in (unauthenticated request), it returns NULL.
-- check authentication
USING (auth.uid() IS NOT NULL AND auth.uid() = user_id)

-- Allow users to SELECT only their own projects
CREATE POLICY "Users can view their own projects"
ON projects
FOR SELECT
USING (auth.uid() = user_id);

-- Allow users to INSERT only their own projects
CREATE POLICY "Users can insert their own projects"
ON projects
FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- Optional: Allow users to UPDATE only their own projects
CREATE POLICY "Users can update their own projects"
ON projects
FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- Optional: Allow users to DELETE only their own projects
CREATE POLICY "Users can delete their own projects"
ON projects
FOR DELETE
USING (auth.uid() = user_id);