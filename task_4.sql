SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'Books'
AND table_schema = 'alx_book_store'