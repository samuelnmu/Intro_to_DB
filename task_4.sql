SELECT 
    COLUMN_NAME AS 'COLUMN',
    COLUMN_TYPE AS 'TYPE',
    IS_NULLABLE AS 'NULLABLE',
    COLUMN_KEY AS 'KEY',
    COLUMN_DEFAULT AS 'DEFAULT',
    EXTRA AS 'EXTRA'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books'
ORDER BY 
    ORDINAL_POSITION;
