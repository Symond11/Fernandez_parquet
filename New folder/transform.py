import duckdb


split = duckdb.sql("""
   SELECT
   SPLIT_PART(browser_os, '|', 1) AS browser,
   SPLIT_PART(browser_os, '|', 2) AS Operating_System 
    
   FROM output.parquet;


    SELECT DISTINCT device_type
    FROM output.parquet; 

   
   SELECT*,
   session_id,
   COALESCE(session_quality_score, avg(session_quality_score)over()) as cleaned_session
   FROM output.parquet;

""")

print(split)