query_insert = "INSERT INTO my_tower.upload_file_cronograma(id, screen, filename) VALUES (%s, %s, %s);"
query_select = "SELECT u.id, u.screen, u.filename FROM my_tower.upload_file_cronograma as u;"