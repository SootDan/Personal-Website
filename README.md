# Personal Website
My personal website written in Python and Flask.  
Backend is stored in PostgreSQL.

## .env variables  
`export PSQL_DATABASE =`  
`export PSQL_USER =`

## PostgreSQL schema
CREATE TABLE IF NOT EXISTS studytime (  
id serial PRIMARY KEY,  
name TEXT,  
required_hours FLOAT,  
studied_hours FLOAT DEFAULT 0,  
deadline DATE)  